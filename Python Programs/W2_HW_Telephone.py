letter = input("Enter a letter? ")
digit = -1
if letter == "A" or letter == "B" or letter == "C":
    digit = 2
elif letter == "D" or letter == "E" or letter == "F":
    digit = 3
elif letter == "G" or letter == "H" or letter == "I":
    digit = 4
elif letter == "J" or letter == "K" or letter == "L":
    digit = 5
elif letter == "M" or letter == "N" or letter == "O":
    digit = 6
elif letter == "P" or letter == "R" or letter == "S":
    digit = 7
elif letter == "T" or letter == "U" or letter == "V":
    digit = 8
elif letter == "W" or letter == "X" or letter == "Y":
    digit = 9
else:
    digit = -1

if digit != -1:
    print("The digit" + " " + str(digit) + " " +"corresponds to the" + " " + letter + " " + "on the telephone")
else:
    print("There is no digit on the telephone that corresponds to" + " " + letter) 
   