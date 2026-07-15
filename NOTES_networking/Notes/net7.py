from netmiko import ConnectHandler
import schedule
import time
device = {
    "device_type": "cisco_ios",
    "host": "192.168.213.200",
    "username": "admin",
    "password": "Cisco123",
}
def monitor_device():
    try:
        print("=" * 50)
        print("Checking device...")

        connection = ConnectHandler(**device)

        output = connection.send_command("show ip interface brief")

        print(output)

        connection.disconnect()

        print("Device is UP")

    except Exception as e:
        print("Device is DOWN")
        print(e)
# Run every 10 seconds
schedule.every(10).seconds.do(monitor_device)

print("Monitoring started...")

# First check immediately
monitor_device()

while True:
    schedule.run_pending()
    time.sleep(1)
