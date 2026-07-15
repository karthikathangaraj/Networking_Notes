from netmiko import ConnectHandler

routers = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.213.200",
        "username": "admin",
        "password": "Cisco123",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.213.201",
        "username": "admin",
        "password": "Cisco123",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.213.202",
        "username": "admin",
        "password": "Cisco123",
    }
]

for router in routers:
    connection = ConnectHandler(**router)

    print(connection.send_command("show running-config | include hostname"))

    connection.disconnect()
