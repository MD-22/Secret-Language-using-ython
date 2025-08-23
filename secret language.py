#secret language project
#Data=Manav
#encyrption=jcbanavMned


#encryption
import random
import string

def encrypt():
    result=""
    for i in range(3):
        result+=random.choice(string.ascii_letters)
    result1=""
    for i in range(3):
        result1+=random.choice(string.ascii_letters)    
    #print(result) 

#n=input("enter ur data:- ")
    if len(n)<=3:
        a=n[::-1]
        print(a)
        print(f"{result}{a}{result1}")
    
    else:
    #print(n[0])
        print(f"{result}{n[1:len(n)]+n[0]}{result1}")


#Now decryption
def decrypt():

#n=input("enter ur data:- ")
    if len(n)<=9:
        a=n[-4:2:-1]
        print(a)
    
    else:
        b=n[3:-3]
        #print(b)
        print(f"{b[-1]}{b[0:-1]}")


#main
n=input("enter ur data:- ")
u=input("encrypt or decrypt:- ")
if(u=="encrypt"):
    encrypt()
else:
    decrypt()