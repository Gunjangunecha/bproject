from flask import Flask, request, jsonify

app = Flask(__name__)

user_data = {
    "full_name": "John Doe",
    "dob": "17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123",
}

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json['data']
        is_success = True  

        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]

        highest_alphabet = []
        if alphabets:
            highest_alphabet = [max(alphabets, key=lambda x: x.lower())]

        response_data = {
            "is_success": is_success,
            "user_id": f"{user_data['full_name']}_{user_data['dob']}",
            "email": user_data["email"],
            "roll_number": user_data["roll_number"],
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet,
        }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run()

