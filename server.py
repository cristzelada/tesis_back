from flask import Flask, request, jsonify
from flask_cors import CORS
from rf import clasification

# Init app
app = Flask(__name__)
CORS(app)


@app.route('/clasification', methods=['POST'])
def get_clasification():
    data = request.get_json()
    x1 = data['weekday']
    x2 = data['chanel']
    x3 = data['typeroom']
    x4 = data['months']
    x5 = data['rooms']
    return jsonify({'clasification': clasification(x1,x2,x3,x4,x5)})


# Run Server
if __name__ == '__main__':
    app.run(debug=True)