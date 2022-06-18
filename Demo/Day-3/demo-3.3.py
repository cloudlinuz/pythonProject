print("Welcome to the dat 3 in python tutorials")

year = int(input("Which year you want to check leap or not? : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The mentioned year is a Leap year")
        else:
            print("The mentioned year is not a Leap Year")
    else:
        print("The mentioned year is a Leap year")
else:
    print("Sorry, The mention year is not a Leap year.")