import random

minor = 100
cont= 0
while cont <= 10:
    number = random.randint(1, 50)
    print(f"the number is: {number}")

    cont = cont + 1
    if number < minor:
        minor = number
print(f"the minor is: {minor}")