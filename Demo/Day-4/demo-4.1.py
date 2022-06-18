import random
import string
import secrets
#
print("Welcome to the Day 4 in python tutorials")

toss = random.randint(0,1)

if toss == 1:
    print("Head")
else:
    print("Tails")

# Password Generator

print("Generation random password with 9 characters")
N = 9
res = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits ) for i in range(N))
result1 = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = N))
print(f"The Random password is : {res}")
print(f"The Random password is : {result1}")
print(f"The Random password is : {''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=N))}")

# This is  the programme for password generator.




