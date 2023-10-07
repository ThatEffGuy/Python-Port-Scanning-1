import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#here we are asking for the target website or host
target = input(' what IP address do you want to scan?: ')

#next line gives us the IP address of the target
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

#function for scanning reports

def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()

#here we are scanning port 0 to 4
for port in range(5):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

end =time.time()
print(f'time taken {end-start:.2f} seconds')




target = input(' what IP address do you want to scan?: ')

target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

def port_scan(port):
        try:
            s.connect((target_ip, port))
            return True
        except:
            return False

start = time.time()

for port in range(5):
        if port_scan(port):
            print(f'port {port} is open')
        else:
            print(f'port {port} is closed')

end =time.time()
print(f'time taken {end-start:.2f} seconds')