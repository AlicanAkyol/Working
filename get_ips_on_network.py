import sys
import os
import threading

ping_parameter = "-n 1"              
threads = []

def ping_ip(host, thread_index):
    ping_result = os.popen("ping " + ping_parameter + " " + host).read()
    if "TTL=" in ping_result:
        print host
    
def create_host(ip):
    for last_block in range(255):
        host = ip + str(last_block)
        siz = len(threads) - 1
        t = threading.Thread(target = ping_ip, args = (host, siz,))
        threads.append(t)
        t.start()
                
if len(sys.argv) == 2:
    create_host(sys.argv[1]) #192.168.1.


#parameter => 192.168.1.
#only Windows
