from flask import Flask
import tweepy
from kafka import KafkaProducer, KafkaConsumer
import json
import nltk
from flask_socketio import SocketIO, send
from dotenv import load_dotenv
from service.StreamListenerImpl import StreamListenerImpl
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

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
        polarity_score = sid.polarity_scores(tweet)
        socketio.emit('polarity_scores', json.dumps(polarity_score))


@app.route('/stop')
def stop_stream():
    streamListener.stop()
    return 'Stopping your stream'


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
    # app.run(host='0.0.0.0')
