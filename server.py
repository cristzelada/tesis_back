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
    x1 = data['weekday']
    x2 = data['chanel']
    x3 = data['typeroom']
    x4 = data['months']
    x5 = data['rooms']
    cls, negative, positive = clasification(x1,x2,x3,x4,x5)
    insert(x1,x2,x3,x4,x5,float(cls), float(positive), float(negative))
    return jsonify({'clasification': float(cls) , 'positive' : float(positive), 'negative' : float(negative)})

@app.route('/clasification', methods=['GET'])
def get_clasifications():
    clasifications = getAll()
    return jsonify(clasifications)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)