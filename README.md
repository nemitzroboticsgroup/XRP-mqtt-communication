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
