# # # # # coding:utf-8 # # # # #
#   Demo no.3                  #
#           zipPasswd+         #
# # # # # # # # # # # # # # # ##

import zipfile
import threading
import optparse

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd = password)
        print('Found Passwd:',password)
    except:
        pass
def main():
    parser  =  optparse.OptionPasrser('usage%prog -f<zipfile>-d <dictionary>')
    passer.add_option('-f' , dest='zname',type='string',help='specofy zip file')
    parser.add_option('-d' , dest='dname',type='string',help='specify dictionart file')
    options,args = parser.parse_arge()
    if options.zname == None|options.dname == None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    dFile =  open(dname,'r')
    for  line in dFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target = extractFile,args  = (zFile,password))
        t.start()
if __name__ == '__main__':
    main()