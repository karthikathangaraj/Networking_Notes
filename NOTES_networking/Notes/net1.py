from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.213.200",
    "username": "admin",
    "password": "Cisco123"
}
connection = ConnectHandler(**R1)

output = connection.send_command("show ip interface brief") 
print(output)

connection.disconnect()
