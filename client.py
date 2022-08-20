
from flask import Flask
from flask import jsonify
from flask import request
import sys
import const 
import requests
# Handle interactive loop



@app.route('/chat',methods=['POST'])
def createEmp():

    data = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    }
    count +=1
    dest_addr = const.registry[data.dest] # get address of destination in the registry
    resposta = requests.post(dest_addr, data=data) #2
    print("RELAYING MSG: " + msg + " - FROM: " + src + " - TO: " + dest) # just print the message and destination
    return jsonify(data)

while True:
    me = str(sys.argv[1]) # User's name (as registered in the registry. E.g., Alice, Bob, ...)
    dest = ''
    id = ''
    reply = input("REPLY? (y or n): ")

    if (reply == 'y'):
        id = input("ENTER MESSAGE ID: ")
    else:
        dest = input("ENTER DESTINATION: ")
    msg = input("ENTER MESSAGE: ")
    
    me = str(sys.argv[1]) # User's name (as registered in the registry. E.g., Alice, Bob, ...)
    data = {
    'dest':dest,
    'name':me,
    'msg':request.json['msg'],
    'ip':const.registry[me][0],
    'id':id
    }
    
    # Send message and wait for confirmation
    resposta = requests.post(const.CHAT_SERVER_HOST, data=data) #2
    if resposta != "ACK":
        print("Error: Server did not accept the message (dest does not exist?)")
    else:
        #print("Received Ack from server")
        pass
