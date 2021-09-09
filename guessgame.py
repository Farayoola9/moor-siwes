# A Number Guessing Game
secret_number = 5
guess_count = 0
guess_limit = 2
while (guess_count < guess_limit):
    guess_number = int(input("Input Guess Number: "))
    guess_count += 1
    if(guess_number == secret_number):
        print("You guessed right")
        break
else:
    print("You are wrong! Try Again")
     
         
