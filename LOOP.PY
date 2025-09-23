total = 0
# # for i in range(1, 20):  
# i = 1
# while(i<20):
#     if i % 2 == 0:       
#         total += i
#     i += 1
 
# print("Sum of even numbers:", total)

# i = 1
# while(i<20):
#     if i % 2 != 0:
#         total += i
#     i += 1 

# print("Sum of odd numbers:", total)

# for i in range(20,0,-1):
    
    
#     print(i)
# list
# len=[2,3,5,7,64,5,5,6,6,6,54,]

# for i in len:
#     print(i)
# # tupple
# t=(2,3,5,7,64,5,5,6,6,6,54,)

# for i in t:
#     print(i) 
    
# # string
# s="hello world" 
# for i in s:
#     print(i)     
    
# l=["make a lot fo momey","buy a house","buy a car","enjoy life","die"]

# for item in l:
#     print(item)
    
# else:
#     print(" loop is over")
 
# n=int(input("Enter a number: "))
# n = int(input("Enter a number: "))
# if n <= 1:
#     print("Number is not prime")
# else:
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             print("Number is not prime")
#             break
#     else:
#         print("Number is prime")

# factorial number program
# n=int(input("Enter a number: "))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print("Factorial of", n, "is", factorial)

# star pattern
n = int(input("Enter the number of rows for the star pattern: "))
for i in range(1, n + 1):
    print(" " * (n-i), end="")
    print("*" * (2*i - 1),end="")
    print()
