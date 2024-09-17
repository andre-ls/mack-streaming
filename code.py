import json
import pandas as pd
from google.cloud import pubsub_v1


def readData(n_messages):
    return pd.read_parquet("data").sample(n_messages)


def generateJson(data):
    return data.to_json(orient='records')

def sendMessage(json_data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('cloud-714', 'mack-streaming')

    for row in json.loads(json_data):
        message = json.dumps(row)
        future = publisher.publish(topic_path, message.encode('utf-8'))
        print(f'Publicando mensagem: {message}')
        print(f'Publicada com ID: {future.result()}')
        print('-'*100)

def publish(n_messages):
    data = readData(n_messages)
    json = generateJson(data)
    sendMessage(json)

if __name__ == "__main__":
    publish(10)
