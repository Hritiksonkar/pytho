a=0
b=1
n=int(input("enter the number"))
if n==0:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n+1):
        c=a+b
        # print this value of c is here
        a=b
        b=c
        print(c)
  
    