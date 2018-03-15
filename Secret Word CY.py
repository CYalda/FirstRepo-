import random

number = random.randint(0,3)

words = ["cat","dog","dragon","bird"]
hint1 = ["chases mice","Barks","breathes fire","flies"]
hint2 = ["can be any color","chases cars","fights knights","many different colors"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess my secret word!")
    print("Type 'hint1','hint2,'first letter', or 'give up' for answer")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) +" guesses.")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint1":
        print( hint2[number] )

    elif guess == "first letter":
        print( secretword[0] )

    elif guess == "give up":
        print("Wow. You gave up.")
        print("You failed" + str(counter) + " times.")
        break

    else:
        print("Guess again.")
        counter +=1


