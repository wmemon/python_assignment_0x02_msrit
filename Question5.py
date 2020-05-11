from time import time
def calc(a,n,m):
    if(n>1):
        if(n%2==0):
            n=n/2
            return (((a**n)**2)%m)
        else:
            n=n-1
            n=n/2
            return ((a*((a**n)**2))%m)


(a,n,m)=input("Enter a,n,m:- ").split(',')
a=int(a)
n=int(n)
m=int(m)
t1 = time()
print("result : ",calc(a,n,m))
t2 = time()
print(f"The time taken is {t2-t1} seconds.")