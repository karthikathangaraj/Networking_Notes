from paramiko import SSHClient, AutoAddPolicy

commands = [
    "show ip interface brief",
    "show version",
    "show clock"
]

for cmd in commands:

    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(
        "192.168.213.200",
        username="admin",
        password="Cisco123"
    )

    stdin, stdout, stderr = client.exec_command(cmd)

    print(f"\nExecuting: {cmd}")
    print(stdout.read().decode())

    client.close()
