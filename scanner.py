#!/bash/python3

import sys
import socket
from datetime import datetime


if len(sys.argv) == 2 :
    target = socket.gethostbyname(sys.argv[1]) #get the second argument of python3 file.py <argument> and translate hostname to ipv4
 
else:
     print("Invalid ammount of arguments")
     print("Syntax: python3 scanner.py <ip>")
     sys.exit()
     
print("-" * 15)
print("scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 15)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
        socket.setdefaulttimeout(1) #if port doesnt open, it will move on
        result = s.connect_ex((target,port))# returns error indicator
        print("Checking port {}".format(port)) 
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to server")
    sys.exit()