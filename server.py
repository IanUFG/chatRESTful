
from flask import Flask
from flask import jsonify
from flask import request
import const 
import requests

app = Flask(__name__)


print("Chat Server is ready...")

count = 1

chatDB=[
]

@app.route('/chat/',methods=['POST'])
def createEmp():

    data = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    }
    
    count +=1
    dest_addr = const.registry[data.dest] # get address of destination in the registry
    resposta = requests.post(dest_addr, data=data) #2
    print("RELAYING MSG: " + data.msg + " - FROM: " + data.name + " - TO: " + data.dest) # just print the message and destination
    return "ACK"

if __name__ == '__main__':
 app.run()