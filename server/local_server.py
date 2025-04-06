# server.py
from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
import openai  # Or replace with your own LLM later

# Initialize
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store connected clients (optional)
connected_clients = set()

@app.route('/')
def serve_index():
    # Serve index.html from the root directory
    return send_from_directory('.', 'index.html')

# @app.route('/')
# def index():
#     return "Raspberry Pi Car Server is running!"

# REST API: send natural language command
@app.route('/send', methods=['POST'])
def send_command():
    user_input = request.json.get("command", "")
    print("Received command:", user_input)

    # Translate using LLM
    # action = parse_with_llm(user_input)
    action = user_input
    
    # Emit to connected Pi clients
    socketio.emit('car_command', {'action': action})
    return jsonify({"sent": action}), 200

# WebSocket: when Raspberry Pi connects
@socketio.on('connect')
def handle_connect():
    connected_clients.add(request.sid)
    print(f"Raspberry Pi connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    print(f"Disconnected: {request.sid}")
    connected_clients.discard(request.sid)

# Sample LLM parser
def parse_with_llm(command):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a command parser for a robot car. Translate user input into actions: 'forward', 'backward', 'left', 'right', 'stop'."},
            {"role": "user", "content": command}
        ]
    )
    return response['choices'][0]['message']['content'].strip().lower()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
