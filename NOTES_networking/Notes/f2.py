from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect(
    hostname="192.168.213.200",
    username="admin",
    password="Cisco123"
)

stdin, stdout, stderr = client.exec_command("show version")

output = stdout.read().decode()

print(output)

client.close()
