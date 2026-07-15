import paramiko
import time

# Router details
HOST = "192.168.213.200"
USERNAME = "admin"
PASSWORD = "Cisco123"

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to router
client.connect(
    hostname=HOST,
    username=USERNAME,
    password=PASSWORD,
    look_for_keys=False,
    allow_agent=False
)

print("Connected Successfully!")

# Open interactive shell
shell = client.invoke_shell()

# Wait for login banner
time.sleep(2)

# Print initial output
if shell.recv_ready():
    print(shell.recv(65535).decode())

# User interaction loop
while True:
    command = input("Enter Cisco Command (type 'exit' to quit): ")

    if command.lower() == "exit":
        break

    # Send command
    shell.send(command + "\n")

    # Wait for router to respond
    time.sleep(2)

    # Read output
    output = ""
    while shell.recv_ready():
        output += shell.recv(65535).decode()

    print("\n========== OUTPUT ==========")
    print(output)

# Close connection
shell.close()
client.close()

print("SSH Connection Closed.")
