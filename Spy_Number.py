n=int(input())
p=1
s=0
while n>0:
    i=n%10
    p=p*i
    s=s+i
    n=n//10
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")