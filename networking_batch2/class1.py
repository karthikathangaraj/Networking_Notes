# class Router:
#     def __init__(self,__hostname,ip,name):
#         self.__hostname=__hostname
#         self.ip=ip
#         self.name=name
#     def show(self):
#         print("HostName",self.__hostname)
#         print("IP address",self.ip) 
#         print("IP address",self.name)      


# r1=Router("cicso","123.1.1.1",1)
# r2=Router("juniper","1.1.1.1",2)
# r3=Router("a","b","c")
# r1.show() 
# # print(r1.__hostname) 


class NetworkDevice:
    name="demo" #class va
    def __init__(self, hostname, ip, status):
        self.hostname = hostname #inst var
        self.ip = ip
        self.status = status

    def show(self):
        print("Hostname :", self.hostname)
        print("IP        :", self.ip)
        print("Status    :", self.status)

    def ping(self):
        print("Pinging", self.ip, "... Success")

router = NetworkDevice("Router1", "192.168.10.1", "Active")

router.show()
router.ping()











