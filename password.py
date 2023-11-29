p=input("Enter the password")
l=0
u=0
d=0
s=0
sp="@,$,#,_"
n=len(p)
for i in s:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
    elif i in sp:
        sp=sp+1
if u>0 and l>0 and d>0 and sp>0 and n>=8:
    print("Password is strong")
elif u>0 or l>0 and d>0 and n>=8:
    print("Password is medium")
elif n>=8:
    print("Password is weak")
else:
    print("Invalid Password")
