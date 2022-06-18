print("Welcome to the day 3 in python tutorials")
height = float(input("Please enter your height in m : "))
weight = float(input("Please enter your weight : "))

bmi = round((weight / height) ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. Your are under weight ")
elif bmi < 25:
    print(f"Your BMI is {bmi}, your are Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, Your are slightly over weight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, Your are obese")
else:
    print(f"Your are BMI is {bmi}, Your are clinically obese")
