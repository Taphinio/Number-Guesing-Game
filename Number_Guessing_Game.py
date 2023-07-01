import random

top_of_range = input("Type a number:")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please typa a number")
    quit()
random_number = random.randrange(top_of_range)
guesses = 0
while True:
    guesses +=1
    user_guess = input("Make a quess:") 
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess < 0:
            print("Pleas type a number larger than 0")
            continue
    else:
        print("Please type a number")
        continue
    if user_guess == random_number:
        break
    else:
        print("You got it wrong")
        if user_guess > random_number:
            print("You were above the random number")
        else:
            print("You were below the random number")
print("You got it in", guesses,"guesses")

    
