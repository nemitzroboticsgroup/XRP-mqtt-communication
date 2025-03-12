import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.client as mqtt
from collections import deque
import matplotlib.animation as animation

# MQTT settings
BROKER = "192.168.1.100"  # Replace with your broker IP
PORT = 1883
TOPICS = [("data/x", 0), ("data/y", 0), ("data/theta", 0)]

# Data buffers
max_points = 100
x_data = deque([], maxlen=max_points)
y_data = deque([], maxlen=max_points)
theta_data = deque([], maxlen=max_points)

# Current values
current_x = 0.0
current_y = 0.0
current_theta = 0.0

# Flags to skip the first received message
skip_first_x = True
skip_first_y = True
skip_first_theta = True

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global current_x, current_y, current_theta
    global skip_first_x, skip_first_y, skip_first_theta
    
    topic = msg.topic
    payload = float(msg.payload.decode())

    if topic == "data/x":
        if skip_first_x:
            skip_first_x = False
            print("Skipping first x")
            return
        current_x = payload
        x_data.append(payload)
        
    elif topic == "data/y":
        if skip_first_y:
            skip_first_y = False
            print("Skipping first y")
            return
        current_y = payload
        y_data.append(payload)
        
    elif topic == "data/theta":
        if skip_first_theta:
            skip_first_theta = False
            print("Skipping first theta")
            return
        current_theta = payload
        theta_data.append(payload)

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_start()

# Plot setup
fig, ax = plt.subplots(figsize=(10, 8))

def animate(i):
    ax.clear()

    if len(x_data) > 0 and len(y_data) > 0:
        ax.plot(list(x_data), list(y_data), linestyle='-', marker='o', markersize=3, label="Trajectory")

        # Plot start and current positions
        ax.scatter(x_data[0], y_data[0], color='green', s=100, label='Start')
        ax.scatter(current_x, current_y, color='red', s=100, label='Current Position')

        # Draw robot orientation arrow
        arrow_length = 2
        arrow_dx = arrow_length * np.cos(current_theta)
        arrow_dy = arrow_length * np.sin(current_theta)

        ax.arrow(current_x, current_y, arrow_dx, arrow_dy,
                 head_width=0.5, head_length=0.5, fc='red', ec='red', label='Orientation')

        # Labels and grid
        ax.set_xlabel("X position (cm)")
        ax.set_ylabel("Y position (cm)")
        ax.set_title("Differential Drive Robot Live Trajectory")
        ax.grid(True)
        ax.axis('equal')

        # Custom legend with live pose info
        current_theta_deg = np.degrees(current_theta)
        pose_label = f"Current Pose:\nX = {current_x:.2f} cm\nY = {current_y:.2f} cm\nθ = {current_theta_deg:.2f}°"
        ax.legend(title=pose_label, loc='best')
    else:
        ax.set_title("Waiting for data...")
        ax.set_xlabel("X position (cm)")
        ax.set_ylabel("Y position (cm)")
        ax.grid(True)
        ax.axis('equal')

ani = animation.FuncAnimation(fig, animate, interval=500)

plt.tight_layout()
plt.show()

# Clean up
client.loop_stop()
client.disconnect()