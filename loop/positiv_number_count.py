num=(1, -2, 3, -4, 5, -6,1, 7, -8, 9, -10)
positive_count=0

for i in num:
    if i>0:
        positive_count+=1

print("Number of positive numbers:", positive_count)    