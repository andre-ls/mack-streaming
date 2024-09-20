# Mack-Streaming

Este repositório contém o trabalho final da Disciplina de Data Collection & Storage, ofertada pelo MBA de Engenharia de Dados da Universidade Presbiteriana Mackenzie.

## Apresentação do Problema

![Taxi](/images/taxi.jpg)
A proposta principal deste trabalho é simples: criar uma arquitetura de streaming capaz de transmitir eventos em tempo real de uma determinada fonte até um destino apropriado.
Para tornar esta proposta um pouco mais próxima de um cenário real, utilizamos como fonte de dados um conjunto de dados público sobre viagens de Taxi realizadas na cidade de Nova York durante o mês de Janeiro de 2024. Com isso, o objetivo do trabalho torna-se criar uma arquitetura capaz de transmitir dados sobre os eventos de corrida em tempo real para uma estrutura de armazenamento adequada para o consumo e análise de dados com uma alta taxa de atualização.
Os dados utilizados contém os seguintes tipos de informação:

## Arquitetura Proposta
Para atender os requisitos apresentados, foi proposta uma arquitetura em nuvem utilizando como sistema central o PubSub, serviço de streaming de mensagens oferecido pelo Google Cloud. O resultado geral da arquitetura, bem como uma breve explicação de cada elemento, podem ser encontrados abaixo.

![Architecture](/images/arquitetura.png)
Figura 1 - Arquitetura Proposta

- Para simular a geração de eventos em tempo real, criamos uma estrutura local com um script Python que lê os dados originais fornecidos pela fonte, amostra uma quantidade de eventos determinada pelo usuário, convertendo-os para um formato JSON e realizando o envio ao PubSub através de um SDK do Google.
- O PubSub, assim como outros serviços de streaming, funciona seguindo uma arquitetura do tipo Publisher-Subscriber, onde a fonte de dados publica a mensagem em um determinado tópico, que geralmente contém dados sobre um mesmo tema, e os consumidores interessados em um determinado tópico consomem as suas mensagens.
- Uma peculiaridade do PubSub, se comparado a outros sistemas de streaming, é que entre o PubSub e os consumidores se encontra um elemento chamado de Inscrição. As inscrições funcionam como filas onde cada mensagem do tópico é fornecida uma única vez, e cada consumidor interessado em obter as mensagens de um tópico precisa obtê-las através de uma inscrição. Vários consumidores podem obter mensagens de uma mesma inscrição, favorecendo o paralelismo no processamento, ou cada consumidor pode ter sua própria inscrição, garantindo assim que cada consumidor receberá as mesmas mensagens.
- Por fim, para armazenar os dados e permitir o seu consumo e análise de maneira eficiente e rápida, utilizamos o BigQuery, solução de Data Warehousing oferecida pelo Google. Uma importante vantagem da sua utilização nessa arquitetura está no fato de que ele possui uma fácil integração com o PubSub a partir da criação de uma inscrição com funcionamento push, ou seja, cada mensagem nova mensagem recebida pelo tópico é automaticamente enviada ao BigQuery, que a adiciona como um novo registro em uma tabela-alvo, criando assim um conjunto de dados que representa um estado dos eventos em tempo real.

## Manual de Utilização

Para reproduzir este projeto, é necessário cumprir alguns requisitos e realizar alguns passos.

### Requisitos
- Possuir uma Conta no Google Cloud
- Criar um Projeto no Google Cloud
- Criar um tópico no PubSub com uma assinatura integrada ao BigQuery
- Criar uma Conta de Serviço com acesso ao PubSub, e gerar uma chave de acesso em formato JSON.

## Passos
- Clonar este repositório.
- Copiar o conteúdo da chave de acesso da Conta de Serviço para o arquivo /auth/gcp_key.json.
- Construir a imagem docker do projeto executando o comando a seguir no diretório raiz:
    ```
    docker build -t mack-streaming .
    ```
- 
