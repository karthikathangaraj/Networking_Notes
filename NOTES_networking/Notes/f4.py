import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname="192.168.213.200",
    username="admin",
    password="Cisco123"
)
stdin, stdout, stderr = client.exec_command("show run | inc host")
output = stdout.read().decode()
print(output)
stdin.write("hello")
client.close()
