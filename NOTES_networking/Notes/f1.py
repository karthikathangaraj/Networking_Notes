from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect(
    "192.168.213.200",
    username="admin",
    password="Cisco123"
)

stdin, stdout, stderr = client.exec_command("show ip interface brief")
print(stdout.read().decode())

client.close()
