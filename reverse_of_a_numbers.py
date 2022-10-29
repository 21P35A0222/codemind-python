n=int(input())
r=0
while n!=0:
    i=n%10
    r=(r*10)+i
    n=n//10
print(r)