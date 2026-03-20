num=int(input("Enter the number: "))
sum=0
for i in range(11):
    if i==5:
        print("5 is skipped")
        continue
    print(num,"X",i,"=",num*i)