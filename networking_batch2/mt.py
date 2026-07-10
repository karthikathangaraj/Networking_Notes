# import threading 
# import time
# def task():
#     for i in range(10):
#         print(threading.current_thread().name,i)
#         time.sleep(1) 

# t1=threading.Thread(target=task)       
# t2=threading.Thread(target=task)  
# t3=threading.Thread(target=task)   
# t1.start()
# t2.start()
import threading
import time

def ping(device):
    print(f"Pinging {device}...")
    time.sleep(2)
    print(f"{device} is reachable")

routers = ["R1", "R2", "R3"]

threads = []

for router in routers:
    t = threading.Thread(target=ping, args=(router,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All routers checked.")

# new --- Runnable -- running --complete







