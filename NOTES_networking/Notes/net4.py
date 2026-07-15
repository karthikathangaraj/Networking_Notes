from netmiko import ConnectHandler

routers = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.213.200",
        "username": "admin",
        "password": "Cisco123"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.213.201",
        "username": "admin",
        "password": "Cisco123"
    }
]

commands = [
    "interface Loopback0",
    "ip address 1.1.1.1 255.255.255.255",
    "no shutdown"
]

for router in routers:
    connection = ConnectHandler(**router)

    print(f"Configuring {router['host']}")

    print(connection.send_config_set(commands))

    connection.disconnect()
