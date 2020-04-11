from tweepy import StreamListener
import json

class StreamListenerImpl(StreamListener):

    def __init__(self, producer):
        super().__init__()
        self.producer = producer

    def on_data(self, raw_data):
        self.producer.send('test', json.loads(raw_data)['text'])

    def on_status(self, status):
        print(status.text)