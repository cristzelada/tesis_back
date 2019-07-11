from flask import Flask, request, jsonify
from flask_cors import CORS
from rf import clasification
from database import insert, getAll

# Init app
app = Flask(__name__)
CORS(app)


@app.route('/clasification', methods=['POST'])
def create_clasification():
    data = request.get_json()
    x1 = data['ReservationMonth']
    x2 = data['ChannelCode']
    x3 = data['TypeRoom']
    x4 = data['LeadTime']
    x5 = data['NumberRooms']
    x6 = data['NumNights']
    x7 = data['RoomRate']
    cls, negative, positive = clasification(x1,x2,x3,x4,x5,x6,x7)
    insert(x1,x2,x3,x4,x5,float(cls), float(positive), float(negative),x6)
    return jsonify({'clasification': float(cls) , 'positive' : float(positive), 'negative' : float(negative)})

@app.route('/clasification', methods=['GET'])
def get_clasifications():
    clasifications = getAll()
    return jsonify(clasifications)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)