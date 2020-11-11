import sys
from rc4 import *
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
ma = Marshmallow(app)
api = Api(app)
  
class Message_Schema(ma.Schema):
    class Meta:
        fields = ("message", "key")
    
message_schema = Message_Schema()

class Cipher_Message(Resource):   
    def post(self):
            message = request.json['message']
            key = request.json['key']
            
            c = encrypt(message, key)
                        
            return jsonify({ "ciphered": "{}".format("".join(c))})
        
class Decipher_Message(Resource):   
    def post(self):
            message = request.json['message']
            key = request.json['key']
            
            d = decrypt(message, key)
                        
            return jsonify({ "deciphered": "{}".format("".join(d))})

api.add_resource(Cipher_Message, '/cipher')     
api.add_resource(Decipher_Message, '/decipher')

if __name__ == '__main__':
    app.run(debug=True)