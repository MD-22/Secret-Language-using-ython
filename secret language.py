#secret language project
#Data=Manav
#encyrption=jcbanavMned
import random
import string
result=""
for i in range(3):
    result+=random.choice(string.ascii_letters)
result1=""
for i in range(3):
    result1+=random.choice(string.ascii_letters)    
#print(result) 


n=input("enter ur data:- ")
if len(n)<=3:
    a=n[::-1]
    print(a)
    print(f"{result}{a}{result1}")
    
else:
    #print(n[0])
    print(f"{result}{n[1:len(n)]+n[0]}{result1}")