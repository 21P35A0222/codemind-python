for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=sorted(b)
    d=min(b)
    e=max(b)
    if b==c:
        print(0)
    else:
        print(e-d)