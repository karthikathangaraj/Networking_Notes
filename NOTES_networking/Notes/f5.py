import paramiko
import time

# Router details
HOST = "192.168.213.200"      # Change to your router IP
USERNAME = "admin"
PASSWORD = "Cisco123"

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=HOST,
    username=USERNAME,
    password=PASSWORD,
    look_for_keys=False,
    allow_agent=False
)

print("Connected Successfully")

shell = client.invoke_shell()
time.sleep(2)
if shell.recv_ready():
    print(shell.recv(65535).decode())

shell.send("show ip interface brief\n")
time.sleep(2)
output = ""

while shell.recv_ready():
    output += shell.recv(65535).decode()

print("========== OUTPUT ==========")
print(output)

# Close SSH connection
shell.close()
client.close()

print("Connection Closed")
