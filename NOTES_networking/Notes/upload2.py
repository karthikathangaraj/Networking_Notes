import paramiko

# Router Details
HOST = "192.168.213.200"
USERNAME = "admin"
PASSWORD = "Cisco123"

# Local file to save the backup
BACKUP_FILE = "/home/gns3/Notes/running_config_backup.txt"

try:
    # Create SSH Client
    client = paramiko.SSHClient()

    # Automatically accept unknown host keys
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the router
    client.connect(
        hostname=HOST,
        username=USERNAME,
        password=PASSWORD,
        look_for_keys=False,
        allow_agent=False
    )

    print("======================================")
    print("Connected Successfully")
    print("======================================")

    # Open interactive shell
    shell = client.invoke_shell()

    # Wait for router prompt
    while not shell.recv_ready():
        pass

    shell.recv(65535)

    # Disable paging
    shell.send("terminal length 0\n")

    while not shell.recv_ready():
        pass

    shell.recv(65535)

    # Execute command
    shell.send("show running-config\n")

    output = ""

    while True:
        if shell.recv_ready():
            data = shell.recv(65535).decode()
            output += data

            # Stop when router prompt returns
            if output.strip().endswith("#"):
                break

    # Save to file
    with open(BACKUP_FILE, "a") as file:
        file.write(output)

    print("Running configuration saved successfully.")
    print("Backup File :", BACKUP_FILE)

    shell.close()
    client.close()

except Exception as e:
    print("Error :", e)
