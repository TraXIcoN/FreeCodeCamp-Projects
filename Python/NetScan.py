from pythonping import ping
import socket

import argparse
import sys

port_common = range(0,255)

# To parse the arguments
def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="Checks if a Host is up or not")
    parser.add_argument("Host", type = str, nargs='+', help = "Host URL/IP Address.")
    parser.add_argument("-p", "--port", type = int, nargs='+', default = port_common, help = "Port number(s) to scan.")
    parser.add_argument("-sp", "--PingScan", help = "Only check if host is/are up.", action='store_true')
    parser.add_argument("-v", "--verbose", help = "Verbose mode.", action='store_true')
    parser.add_argument("-f", "--force", help = "Assume that the host is up.", action='store_true')
    #parser.add_argument("-t", "--test", type=int, help = "test flag")
    
    options = parser.parse_args(args)
    
    return options

# To test if the host is online
def ping_test( host, verb ):
    try:
        ping(host, verbose=verb)
        return True
    except (RuntimeError):
        return False

# To check if a port is listening or not
def port_check( host, port, verb):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(2)
        s.connect((host, port))
        print ("Host:", host, "Port:", port, "is reachable.")
    except socket.error:
        if verb:
            print ("Host:", host, "Port:", port, "is not reachable")
    s.close()
args = getOptions()
print(args)

hosts = args.Host       # Host(s)
verb = args.verbose     # Verpose Flag
force = args.force      # Force (Ping Sweep) Flag
ports = args.port       # Port(s) to scan
ps = args.PingScan      # Ping Scan flag

anyUp = False           # Internet Connection test flag

if force == False :
    for host in hosts :

        if ping_test( host, verb ) :
            print ("Host: " + host + " is up.")
            if ps == False :
                for port in ports :
                    port_check( host, port, verb )
            anyUp = True

        else:
            print ("Host: " + host + " is down.")

else :
    if ps == False :
        for host in hosts :
            for port in ports :
                port_check( host, port, verb )

if anyUp == False and ping_test( "google.com", False ) == False :
    print( "Your internet connection seems down!" )

