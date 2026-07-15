import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname="192.168.213.202",
    username="admin",
    password="Cisco123"
)

stdin, stdout, stderr = client.exec_command("show running-config")
output = stdout.read().decode()
with open("backup.txt", "a") as file:
    file.write(output)
print("Backup Saved")

client.close()
