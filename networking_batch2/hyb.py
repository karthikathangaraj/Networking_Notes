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


class Firewall(NetworkDevice):
    def filter_traffic(self):
        print("Filtering network traffic...")

class SecureRouter(Router, Firewall):
    def vpn(self):
        print("VPN Enabled")        
sr = SecureRouter("SR1", "192.168.1.100")

sr.show_info()
sr.route()
sr.filter_traffic()
sr.vpn()
