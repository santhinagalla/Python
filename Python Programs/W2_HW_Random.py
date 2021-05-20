import random
randomnumber = random.randint(1, 20)
print('I am think of a number between 1 and 20 ' + str(randomnumber))
guessnumber = int(input("Can you guess what it is? "))
max_tries = 5
counter=1
while True:
    if (guessnumber == randomnumber):
        print("Congratulations! You did it.") 
        break
    elif counter < max_tries:
        if(guessnumber > randomnumber):
            guessnumber=int(input("Your guess is high. Try again: " ))
            counter = counter +  1
        else:
            guessnumber=int(input("Your guess is low. Try again: " ))
            counter = counter +  1
    else:
        print("Sorry. The number was" + " " + str(randomnumber) + " " + "You should have gotten it by now." + " " + "Better luck next time.")
        break