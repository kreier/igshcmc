from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple hello world endpoint.
    ---
    responses:
      200:
        description: Returns a greeting message
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify({"message": "Hello, World!"})

@app.route('/add', methods=['POST'])
def add_numbers():
    """
    Add two numbers.
    ---
    parameters:
      - name: a
        in: query
        type: integer
        required: true
        description: First number
      - name: b
        in: query
        type: integer
        required: true
        description: Second number
    responses:
      200:
        description: The sum of the two numbers
        examples:
          application/json: {"sum": 5}
    """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"sum": a + b})

if __name__ == "__main__":
    app.run(debug=True)
