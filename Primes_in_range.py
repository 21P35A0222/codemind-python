def primes(a):
    if a==0 or a==1:
        return 0
    for i in range (2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for j in range(a,b+1):
    if primes(j):
        c+=1
print(c)