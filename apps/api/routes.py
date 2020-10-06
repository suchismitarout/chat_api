from flask import jsonify, request
import logging

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

users_list = []
msg_info = {}

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
app.config["CORS_SUPPORTS_CREDENTIALS"] = True


@app.route('/users', methods=['POST'])
def add_users():
    data = request.get_json()
    users_list.append(data)
    logging.info("ENTRY: received data .{}".format(data))

    # hardcoded. to be changed later
    resp = {'message': 'successful'}
    return jsonify(data)


@app.route('/getusers', methods=['GET'])
def get_users():
    return jsonify(users_list)


@app.route('/msg', methods=['POST'])
def send_message():
    message = request.get_json()
    msg_info[message['to']] = message['msg']
    logging.info(msg_info)
    logging.info("....msg received {}".format(message))
    return jsonify(message)


@app.route('/msg', methods=['GET'])
def get_all_messages():
    logging.info("get messages")
    return jsonify(msg_info)
    # for i in msg_info:
    #     return jsonify(i)


@app.route('/msg/<name>', methods=['GET'])
def get_messages_by_name(name):
    logging.info(".......get msg by name")
    if name in msg_info:
        logging.info(msg_info[name])
        return jsonify(msg_info[name])
