import json
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.213.200",
    "username": "admin",
    "password": "Cisco123",
    "secret": "Cisco123"
}
connection = ConnectHandler(**device)
connection.enable()
running_config = connection.send_command("show running-config")
version = connection.send_command("show version")
interfaces = connection.send_command("show ip interface brief")
connection.disconnect()

backup = {
    "hostname": device["host"],
    "running_config": running_config,
    "version": version,
    "interfaces": interfaces
}
with open("R1_backup.json", "a") as file:
    json.dump(backup, file, indent=4)

print("Backup saved as R1_backup.json") 
