print("Welcome to the day 3 in python tutorials")
height = int(input("Please enter your height in cm? : "))
bill = 0
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Please enter your age : "))
    if age < 12:
        bill = 5
        print("You can pay $5")
    elif age <= 18:
        bill = 7
        print("You can pay $7")
    elif age <= 40:
        bill = 12
        print("You can pay $12")
    elif age >= 45 and age <= 56:
        bill = 0
        print("You have eligible fo free ticket")
    else:
        bill = 20
        print("You can pay $20")
    photos = input("Do you want photo. Press Y or N : ")
    if photos == "Y":
        print("You want to pay extra $3 ")
        bill += 3
    print(f"You total bill is ${bill}")
else:
    print("You can't ride the roller coaster ")
