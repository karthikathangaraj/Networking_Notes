import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname="192.168.213.200",
    username="admin",
    password="Cisco123"
)
sftp = client.open_sftp()
local_file = "/home/gns3/Notes/t1.txt"
remote_file = "/home/admin/backup.txt"

sftp.put(local_file,remote_file)
print("File Uploaded Successfully")

sftp.close()
client.close()
