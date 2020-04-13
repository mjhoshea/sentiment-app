from tweepy import StreamListener
import json

class StreamListenerImpl(StreamListener):

    def __init__(self, producer):
        super().__init__()
        self.producer = producer
        self.contin = True

    def on_data(self, raw_data):
        if(self.contin == False):
            return False
        self.producer.send('test', raw_data)

    def on_status(self, status):
        print(status.text)

    def stop(self):
        self.contin = False

    def start(self):
        self.contin = True
