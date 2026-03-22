input_str = "hello world"
for char in input_str:
    if input_str.count(char) == 1:
        print(f"The first unique character is: '{char}'")