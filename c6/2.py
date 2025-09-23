marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))
marks4 = int(input("Enter your marks: "))

tatol_parcentege = (marks1 + marks2 + marks3 + marks4) / 4
if tatol_parcentege >= 90:
    print("A+")
elif tatol_parcentege >= 80:
    print("A")
elif tatol_parcentege >= 70:
    print("B")          
elif tatol_parcentege >= 30:
    print("you can to next year")          