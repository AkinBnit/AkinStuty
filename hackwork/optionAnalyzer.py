# # # # # coding:utf-8 # # # # #
#       Day:1 socker TCP       #
# # # # # # # #### # # # # # # #

import socket
import optparse

parser = optarse.OptionParse('usage % prog -H <targethost> -p <target port>')

parser.add_option('-H',dest = 'tgtHost',type = 'string',help ='specify  target host')

parser.add_option('-p',dest = 'tgtPort',type = 'int',  help = 'specify target prot')

(options,args) = parser.parse_arge()
tgtHost = options.tgtHost
tgtProt = options.tgtPort

if (tgtHost == None)|(tgtPort == None):
    print(parser.usage)
    exit(0)
else:
    print(tgtHost)
    print(tgtPort)