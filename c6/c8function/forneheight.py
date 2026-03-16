def f_to_c(f):
    c = (f - 32) * 5/9
    return c
f = float(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"The temperature in Celsius is: {c:.2f} °C")
