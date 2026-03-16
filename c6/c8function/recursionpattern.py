# def pattern(n):
#     if n > 0:
#         pattern(n - 1)
#         print('*' * n)
# pattern(5)

def inches_to_cm(inches):
    cm = inches * 2.54
    return cm
n=int(input("Enter length in inches: "))
print(f"{n} inches is equal to {inches_to_cm(n)} cm")