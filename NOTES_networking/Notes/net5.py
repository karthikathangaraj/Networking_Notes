from netmiko import ConnectHandler

connection = ConnectHandler(**device)

connection.enable()

commands = [
    "interface Loopback0",
    "ip address 1.1.1.1 255.255.255.255",
    "no shutdown"
]

connection.send_config_set(commands)   # Configure router

connection.save_config()               # Save permanently

connection.disconnect()   
