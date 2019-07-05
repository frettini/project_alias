# Socket I/O
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

from modules import globals
from modules import settings

import logging

# Socket I/O
#====================================================#
PORT            = 5050
HOST            = '0.0.0.0'
app             = Flask(__name__)
app.debug       = False
socketio        = SocketIO(app, async_mode='threading', logger=False)
socket_thread   = None
FLASK_DEBUG = 0
logging.getLogger('werkzeug').setLevel(logging.ERROR) # remove socket io logs

def sendMsg(namespace,obj):
    socketio.emit(namespace,obj,namespace='/socket')

# def sendMsgComp(namespace, obj):
#     socketio.emit(namespace, obj, namepspace='/computer')

@app.route('/')
def index():
    print('Someone Connected!')
    sendMsg('response',settings.read())
    return render_template('index.html')

@socketio.on('connect')
def connect():
    socketio.emit('my response', {'data': 'Connected'})

# @app.route('/computer')
# def computer():
#     print('computer connected!')
#     sendMsgComp('response', data = 1)


