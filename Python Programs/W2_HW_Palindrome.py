readnumber= int(input("Read a number?  "))
originalnumber = readnumber
reversenumber = 0
while readnumber > 0:
    remainder=int(readnumber%10)
    reversenumber= reversenumber *10 + remainder
    readnumber =int(readnumber/10)

if(originalnumber == reversenumber):
    print("It is palindrome")
else:
    print("It is not a palindrome")