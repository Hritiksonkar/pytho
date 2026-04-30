num =10
result = []
for i in range (1,num//2):
    if num%i==0:
        result.append(i)
print(f"The factors of {num} are: {result}")