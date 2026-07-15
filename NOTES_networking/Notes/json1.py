import json

device = {
    "hostname": "R1",
    "ip": "192.168.213.200",
    "vendor": "Cisco"
}
print(type(device))
print(type(json.dumps(device, indent=4)))
