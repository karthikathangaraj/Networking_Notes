from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.213.200",
    "username": "admin",
    "password": "Cisco123"
}
connection = ConnectHandler(**device)

commands = [
    "interface FastEthernet0/1",
    "ip address 192.168.213.203 255.255.255.0",
    "no shutdown"
]

output = connection.send_config_set(commands)
print(output)
connection.disconnect()
