n=int(input())
l=[]
while n!=0:
    i=n%10
    l.append(i)
    n=n//10
print(max(l))