from flask import Flask, request
import tweepy
from StreamListenerImpl import StreamListenerImpl


app = Flask(__name__)

consumer_key='yZst27GNzlTDMVnxw5qKPTp53'
consumer_secret='1Mh6ZqmZ042YAjeyf5cZujGbY99NrtTuvP5lVgX3T0OAoj7Sis'
access_token='1175398657765576704-zPdSrh590OGC3wPHQRljTJTbbyecaG'
access_token_secret='aLUpTCTU8mbZ9omZVs6CCrMJR8qOW4LglCIMihrjYRpKD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


streamListener = StreamListenerImpl()
myStream = tweepy.Stream(auth=api.auth, listener=streamListener)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/track/<topic>')
def hello_boris(topic):
    print(topic)
    myStream.filter(track=[topic], is_async=True)
    return 'Getting Your Topic'

if __name__ == '__main__':



    app.run()
