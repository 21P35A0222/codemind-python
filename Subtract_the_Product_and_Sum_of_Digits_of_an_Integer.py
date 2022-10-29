n=int(input())
p=1
s=0
while n>0:
    i=n%10
    s=s+i
    p=p*i
    n=n//10
print(abs(p-s))