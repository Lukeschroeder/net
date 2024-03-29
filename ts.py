import sys
from networking import Server
infilename = 'PROJI-DNSTS.txt'
DNStable = {}
datalength = 200


# Fills in DNS table with entries from file 
def populateDNStable():
    infile = open(infilename, 'r')
    lines = infile.readlines()
    for index in range(len(lines)):
        DNSentry = lines[index].split()
        DNStable[DNSentry[0].lower()] = DNSentry



def queryDNStable(server):
    while(True):
        # Receive message from client
        hostname = server.activesocket.recv(datalength)
        if len(hostname) == 0: break
        if DNStable.has_key(hostname):
            DNSentry = DNStable[hostname]
            response = DNSentry[0] + ' ' + DNSentry[1] + ' ' + DNSentry[2]
            server.activesocket.send(response.encode('utf-8'))
        else:
            response = hostname + ' - Error:HOST NOT FOUND'
            server.activesocket.send(response.encode('utf-8'))



def main():
    args = sys.argv
    if len(args) != 2: print 'Insufficient Arguments'

    tsListenPort = int(args[1])

    populateDNStable()
    server = Server(tsListenPort)
    server.accept()
    queryDNStable(server)
    server.close()

    
   
        
if __name__ == "__main__":
    main()




