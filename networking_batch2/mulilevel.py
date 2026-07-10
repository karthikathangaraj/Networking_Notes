class NetworkDevice:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def show_info(self):
        print("Hostname:", self.hostname)
        print("IP Address:", self.ip)
class Router(NetworkDevice):
    def route(self):
        print("Routing packets...")

class CiscoRouter(Router):
    def route(self):
        print("Routing packets... i am in cisco")
    def configure_vlan(self):
        print("Configuring VLAN on Cisco Router...",self.hostname)

r1 = CiscoRouter("R1", "192.168.1.1")
r4=Router("1","1")
r4.route()
r1.route()
# r1.show_info()
# r1.route()
r1.configure_vlan()