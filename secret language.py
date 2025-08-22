#secret language project
#Data=Manav
#encyrption=jcbanavMned
n=input("enter ur data:- ")
if len(n)<=3:
    a=n[::-1]
    print(a)
else:
    print(n[0])
    print (n[1:len(n)]+n[0])