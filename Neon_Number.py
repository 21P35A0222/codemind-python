n=int(input())
m=n*n
s=0
while m>0:
    i=m%10
    s=s+i
    m=m//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")