import yaml

devices = {
    "devices": [
        {
            "hostname": "R1",
            "device_type": "cisco_ios",
            "host": "192.168.213.200",
            "username": "admin",
            "password": "Cisco123"
        },
        {
            "hostname": "R2",
            "device_type": "cisco_ios",
            "host": "192.168.213.201",
            "username": "admin",
            "password": "Cisco123"
        },
        {
            "hostname": "R3",
            "device_type": "cisco_ios",
            "host": "192.168.213.202",
            "username": "admin",
            "password": "Cisco123"
        }
    ]
}
with open("devices.yaml", "a") as file:
    yaml.dump(devices, file, default_flow_style=False)

print("devices.yaml created successfully!")
