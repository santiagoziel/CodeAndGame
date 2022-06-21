from flask import request
from flask_socketio import emit, join_room, leave_room

from dta_pkt import socketio, db
from dta_pkt.routes import current_user
from dta_pkt.models import User

#when user conects to the socket it changes his room number from empty to his current room
#and lets evrybody know a new user conected
@socketio.on('connect')
def user_conecting():
    current_user.room = request.sid
    db.session.commit()
    new_user = User.query.filter(User.room == request.sid).first()
    emit('new active user', new_user.username, broadcast=True)

#when recibing message form cleint sent it to that cleint room
@socketio.on('new message')
def handle_message(data):
    # TODO: make it so its sends to current user room
    emit('incoming message', {'message' :data['message']})
#when clint disconects it removes his room from the database
@socketio.on('client_disconnecting')
def disconnect_details(data):
    current_user.room = ""
    db.session.commit()
    emit('remove active user', current_user.username, broadcast=True)

@socketio.on('whants to talk to')
def stablish_room_conection(talkto_name):
    talkto = User.query.filter(User.username == talkto_name).first()
    #join this socket to talkto_room
    join_room(talkto.room)
    #send event to talkto_room to join current_user_room
    emit('whants to talk',current_user.room, to=talkto.room)

@socketio.on('whants to stop talking to')
def remove_room_conectino(talkto_name):
    talkto = User.query.filter(User.username == talkto_name).first()
    leave_room(talkto.room)
    emit('stop talk',current_user.room, to=talkto.room)

@socketio.on('talk to me')
def talk_back(room):
    join_room(room)
    talkto = User.query.filter(User.room == room).first()
    emit('conection updated', f"{talkto.username} is now talking with {current_user.username}")

@socketio.on('stop talking to me')
def stop_talk(room):
    leave_room(room)
    talkto = User.query.filter(User.room == room).first()
    emit('conection updated', f"{talkto.username} stoped talking with {current_user.username}")
