import paramiko
import time

# Router details
host = "192.168.213.202"      # Change to your router IP
username = "admin"
password = "Cisco123"

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to router
    client.connect(
        hostname=host,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False
    )

    print("Connected Successfully!\n")

    # Start interactive shell
    shell = client.invoke_shell()

    # Wait for prompt
    time.sleep(2)

    # Clear initial banner
    if shell.recv_ready():
        print(shell.recv(65535).decode())

    # Commands to execute
    commands = [
        "configure terminal",
        "hostname PYTHON-R3",
        "interface FastEthernet0/0",
        "description Configured by Paramiko",
        "end",
        "write memory"
    ]

    # Send commands one by one
    for cmd in commands:
        print(f"Executing: {cmd}")

        shell.send(cmd + "\n")
        time.sleep(1)

        output = ""

        while shell.recv_ready():
            output += shell.recv(65535).decode()

        print(output)

    # Verify configuration
    shell.send("show running-config interface FastEthernet0/0\n")
    time.sleep(2)

    output = ""
    while shell.recv_ready():
        output += shell.recv(65535).decode()

    print("Verification Output:")
    print(output)

except Exception as e:
    print("Error:", e)

finally:
    client.close()
    print("SSH Connection Closed.")
