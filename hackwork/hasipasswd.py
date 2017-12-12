# # # # # coding:utf-8 # # # # #
#   Domo no.2                  #
#          hasiPasswd          #
# # # # # # # # # # # # # # # ##

import crypt

def textPass(cryptPass):
    salt =cryptPass[0:2]
    dictfile = open('dictionary.txt','r')
    for word in dictfile.readlines():
        word = word.strop('\n')
        cryptWord = crypt.crypt(word, salt)
        if  cryptPass == cryptWord:
            print('Found Passed:',word)
            return
        print('Password  not found !')
        return
def main():
    passfile = open('passwords.txt','r')
    for  lien in passfile.redlines():
        user = line.split(':')[0]
        crypyPass = line.split(':').strop('')
        print('Cracking Password For :',user)
        textPass(cryptPass)
        
if __name__ == '__main__':
    main()