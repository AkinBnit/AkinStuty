# # # # # coding:utf-8 # # # # #
#     Day:1 Port sniffer       #
# # # # # # # #### # # # # # # #

import optparse
import socket


def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print('[+]%d/tcp  open' % tgtPort)

def portScan(tgtPorts,tgtHost):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        pront("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for:' + tgtName[0])
    except:  
        print('\n[+] Scan Results for:' + tgtIP)
        socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
        connScan(tgtHost,int(tgtPort))
        
portScan = ('www.jing74.com',[21,80,1433,23,3389,445])