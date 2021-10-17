from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
import threading 
import base64

def encodeImgDict(imgDict):
    imgFile = open(imgDict['link'],'rb')
    encoded_str = base64.b64encode(imgFile.read())
    imgDict['link'] = encoded_str.decode('utf-8')
    imgFile.close()
    return imgDict

imageDicts = [ { "idx": 0, "link": 'pics/1.png' },
  { "idx": 1, "link": 'pics/2.png' },
  { "idx": 2, "link": 'pics/3.png' },
  { "idx": 3, "link": 'pics/4.png' },
  { "idx": 4, "link": 'pics/5.png' },
  { "idx": 5, "link": 'pics/6.png' },
  { "idx": 6, "link": 'pics/7.png' },
  { "idx": 7, "link": 'pics/8.png' },
  { "idx": 8, "link": 'pics/9.png' },
  { "idx": 9, "link": 'pics/10.png' },
  { "idx": 10, "link": 'pics/11.png' } ]

for imageDict in imageDicts:
    imageDict = encodeImgDict(imageDict)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socket = SocketIO(app,  cors_allowed_origins="*",  engineio_logger=True, logger=True)

gData = {}
@socket.on('connect')
def onConnect(data):
    emit('connect', imageDicts[0])
@socket.on('send')
def onFetch(data):
    if(data.get('idx') == 10):
        idx = 0
    else:
        idx = data.get('idx') +1
    emit('fetch', imageDicts[idx])
    

