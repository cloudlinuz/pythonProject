print("Welcome to the pizza deliveries")
pizza_size = input("What size do you want? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N :  ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
bill = 0

if pizza_size == "S":
    bill += 15
    print("You ordered Small size of pizza")
elif pizza_size == "M":
    bill += 20
    print("You ordered Medium size of Pizza")
else:
    bill += 25
    print("You ordered Large size of Pizza")

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")



