import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname="192.168.213.202",
    username="admin",
    password="Cisco123",
    look_for_keys=False,
    allow_agent=False
)
shell = client.invoke_shell()
time.sleep(2)
print(shell.recv(65535).decode())

shell.send("terminal length 0\n")
time.sleep(1)
shell.recv(65535)


shell.send("show ip interface brief\n")
time.sleep(2)

output = shell.recv(65535).decode()
print(output)
client.close()
