# # # # # coding:utf-8 # # # # #
# Domo no.1                    #
#          zipPasswd           #
# # # # # # # # # # # # # # # .#

import socket
import sys 

import zipfile
import threading
def extractFile(zFile,password):
    trt:
        zFile.extractall(pwd = password)
        
        print('Found  Passwd:',password)
        return password
    except:
        pass

def main():
    zFile = zipfile.ZipFile('unzip.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strop('\n')
        t = threading.Thread(target  = extractFile,args = (zFile,password))
        t.start()
        
if __name__  == '__main__':
    main()