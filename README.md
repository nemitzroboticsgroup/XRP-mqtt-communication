# XRP MQTT Communication

Library and example code for using MQTT with the XRP robot.

## MQTT Broker

You will need an MQTT broker running on a Wi-Fi network that the XRP robot can also access.

## Configuration

Ensure the XRP robot connects to the same Wi-Fi network as the MQTT broker.

1. Edit `config.txt` and add your Wi-Fi **SSID** and **Password**.
2. Add the MQTT broker's **IP address** to both `config.txt` and `mqttconnect.py`.

## MQTT Explorer (Optional)

For testing and debugging, consider installing [MQTT Explorer](https://mqtt-explorer.com).

- Make sure your laptop is connected to the same Wi-Fi network as the broker.
- MQTT Explorer lets you easily subscribe to and publish messages on topics to interact with the XRP robot.

## XRP Robot Live Trajectory Plotter (MQTT)

This script subscribes to MQTT topics and plots the live trajectory and orientation of an XRP robot in real-time.  
It uses `matplotlib` for visualization and `paho-mqtt` for MQTT communication.

### What the XRP Robot Needs to Do

The XRP robot must publish three key values over MQTT in real time:
1. **X position**  
2. **Y position**  
3. **Theta (orientation in radians)**

### Expected MQTT Topics
- `data/x` ➜ X coordinate (in centimeters or meters)
- `data/y` ➜ Y coordinate (in centimeters or meters)
- `data/theta` ➜ Orientation angle in **radians**

### Example of what the XRP should publish
- `c.publish("data/x", str(current_x), retain=True)`
- `c.publish("data/y", str(current_y), retain=True)`
- `c.publish("data/theta", str(current_theta), retain=True)`

### How to Use the Script

#### Make sure you have Python 3 and install the required libraries:
```bash
pip install matplotlib paho-mqtt
```

#### Modify the MQTT Broker Address in the Script
BROKER = "192.168.1.100"

#### Run the Program
```bash
python3 plot_data_live_mqtt.py
```

