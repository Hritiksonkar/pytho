p1="make a lot fo momey"
p2="buy a house"
p3="buy a car"
p4="enjoy life" 
p5="die"

message= input("Enter your message: ")
if (p1 in message or p2 in message or p3 in message or p4 in message or p5 in message):
    print("you are a very ambitious person")
    
else:
    print("you are a simple person")