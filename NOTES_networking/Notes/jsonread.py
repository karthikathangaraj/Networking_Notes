import json
from netmiko import ConnectHandler

# Load JSON configuration
with open("config.json", "r") as file:
    config = json.load(file)

devices = config["devices"]
commands = config["commands"]

for device in devices:
    print(f"\nConnecting to {device['host']}...")

    try:
        connection = ConnectHandler(**device)

        # Enter enable mode
        connection.enable()

        # Execute commands
        for command in commands:
            print(f"\n>>> {command}")
            output = connection.send_command(command)
            print(output)

        connection.disconnect()
        print("\nDisconnected")

    except Exception as e:
        print("Connection Failed:", e)
