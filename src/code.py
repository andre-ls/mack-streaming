import json
import argparse
import pandas as pd
from google.cloud import pubsub_v1

def readData(n_messages):
    return pd.read_parquet("data").sample(n_messages)

def generateJson(data):
    return data.to_json(orient='records')

def sendMessage(google_project, pubsub_topic, json_data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(google_project, pubsub_topic)

    for row in json.loads(json_data):
        message = json.dumps(row)
        future = publisher.publish(topic_path, message.encode('utf-8'))
        print(f'Publicando mensagem: {message}')
        print(f'Publicada com ID: {future.result()}')
        print('-'*100)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--google_project", required=True)
    parser.add_argument("--pubsub_topic", required=True)
    parser.add_argument("--n_messages", default=10)
    args = parser.parse_args()

    data = readData(args.n_messages)
    json_data = generateJson(data)
    sendMessage(args.google_project, args.pubsub_topic, json_data)
