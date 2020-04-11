from tweepy import StreamListener


class StreamListenerImpl(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)

    def on_status(self, status):
        print(status.text)