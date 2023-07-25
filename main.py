from flask import Flask, request

app = Flask(__name__)


# POST endpoint at /test
@app.route('/test', methods=['POST'])
def test_endpoint():
    # Get the JSON data from the POST request
    data = request.json

    # Process the data (you can add your own logic here)
    if data is not None:
        response = {'message': 'Data received successfully', 'data': data}
        return response, 200
    else:
        return {'error': 'No data received'}, 400


if __name__ == '__main__':
    app.run(port=8080)
