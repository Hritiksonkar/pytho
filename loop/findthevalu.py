nums =(1,4,9,12,3,2,5,6,7,8,1,11)

x=1
i=0

while i<len(nums):
    if (nums[i]==x):
        print("Index of the value is: ", i)
    i+=1
    
    
# prime number
number=  int(input("Enter a number: "))
is_prime=True
if number>1:
    for i in range(2, number):
        if number%i==0:
            is_prime=False
            break
print( is_prime)