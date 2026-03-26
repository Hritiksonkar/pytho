input_str = "teeteracdacd"
for char in input_str:
    if input_str.count(char) == 1:
        print(f"The first unique character is: '{char}'")
        
# foctorial number using loop 
number=5
factorial=1
while number>0:
    factorial *= number
    number -= 1
print(f"The factorial ", factorial)