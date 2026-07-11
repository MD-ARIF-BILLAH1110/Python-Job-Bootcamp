import random

#using random modules for random number
computer = random.randint(1, 10)

#take input from user
user = int(input("Guess the number (1, 10): "))

while user != computer:

    if user < computer:
       print("Too Low")
      
    elif user > computer:
       print("Too High")
    
    user = int(input("Guess again: "))

print(f"🎉 Congratulations! The number was {computer}.")
       
   