# pi_client.py
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.on('car_command')
def on_car_command(data):
    action = data.get('action', '')
    print("Received action:", action)
    execute_action(action)

@sio.event
def disconnect():
    print('Disconnected from server')

def execute_action(action):
    # This is where you control motors (GPIO)
    if action == "forward":
        print("Moving forward")
        # call_motor_forward()
    elif action == "backward":
        print("Moving backward")
    elif action == "left":
        print("↪Turning left")
    elif action == "right":
        print("↩Turning right")
    elif action == "stop":
        print("Stopping")
    else:
        print("Unknown command:", action)

# Connect to server
sio.connect('http://192.168.0.87:5001')
sio.wait()
# http://192.168.0.87:5001
