from flask import Flask
import tweepy
from kafka import KafkaProducer, KafkaConsumer
import json
import nltk

from service.StreamListenerImpl import StreamListenerImpl

app = Flask(__name__)

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

consumer_key='yZst27GNzlTDMVnxw5qKPTp53'
consumer_secret='1Mh6ZqmZ042YAjeyf5cZujGbY99NrtTuvP5lVgX3T0OAoj7Sis'
access_token='1175398657765576704-zPdSrh590OGC3wPHQRljTJTbbyecaG'
access_token_secret='aLUpTCTU8mbZ9omZVs6CCrMJR8qOW4LglCIMihrjYRpKD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

streamListener = StreamListenerImpl(producer)
myStream = tweepy.Stream(auth=api.auth, listener=streamListener)


@app.route('/')
def home():
    return 'To begin analysing a topic go to localhost:5000/track/<topic>'


@app.route('/track/<topic>')
def track_topic(topic):
    streamListener.start()
    myStream.filter(track=[topic], is_async=True)
    return 'Getting Your Topic'

@app.route('/analyse/<topic>')
def analysis_topic(topic):
    print(topic)
    consumer = KafkaConsumer('test', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for mes in consumer:
        tweet = json.loads(mes.value)['text']
        print('                         ')
        print('-------------------------')
        print(tweet)
        print(sid.polarity_scores(tweet))
        print('-------------------------')
        print('                         ')


@app.route('/stop')
def stop_stream():
    streamListener.stop()
    return 'Stopping your stream'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
