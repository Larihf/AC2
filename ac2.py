from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {
        "id": 1,
        "produto": 'product1'
    },
    {
        "id": 2,
        "produto": "product2"
    }
]



@app.route('/', methods=["GET"])
def home():
    return jsonify(produtos), 200

app.run(debug=True)