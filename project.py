computer=-1
youstarted=-1   
while computer==-1 or youstarted==-1:
    computer=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    youstarted=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
if computer==youstarted:
    print("It's a tie!")    
elif (computer==0 and youstarted==2) or (computer==1 and youstarted==0) or (computer==2 and youstarted==1):
    print("Computer wins!")
else:
    print("You win!")
#  --- IGNORE ---1
