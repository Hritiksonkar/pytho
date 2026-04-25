n=12345
num=n
result=0
while num>0:
    rem=num%10
    result=result*10+rem
    num=num//10
if result==n:
    print(n, "is a palindrome") 
else:   
    print(n, "is not a palindrome")
