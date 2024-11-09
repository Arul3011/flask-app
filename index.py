from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database
data_store = []

@app.route('/data', methods=['GET'])
def get_data():
    """Retrieve all data from the data store."""
    return jsonify(data_store), 200

@app.route('/data', methods=['POST'])
def post_data():
    """Add new data to the data store."""
    new_data = request.json  # Get the JSON data from the request
    if not new_data:
        return jsonify({"error": "No data provided"}), 400
    
    data_store.append(new_data)  # Store the new data
    return jsonify(new_data), 201  # Return the newly added data with a 201 status code

if __name__ == '__main__':
    app.run(debug=True)
