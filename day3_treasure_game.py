# if / else Statements
water_level = int(input())
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

water = input("what is your water?")

try:
    if water>=80:
        print("drain")
    else:
        print("not")
except:
    print("invalid")

height = int(input("what is your height?"))  #must convert to int not str to compare with a number

if height>=120:
    print("can ride")
else:
    print("can't ride")

# Write a program that works out whether if a given number is an odd or even number.
# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if number%2==0:
  print("This is an even number.")
else:
  print("This is an odd number.")

height = int(input("what is your height?"))  # must convert to int not str to compare with a number

if height >= 120:
    print("can ride")
    age = int(input("How old are you?"))
    if age < 12:
        print("Your cost is 5$")
    elif age <= 18:
        print("Your cost is 7$")
    else:
        print("Your cost is 12$")
else:
    print("can't ride")

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight = float(input("what is your weight?"))
height = int(input("what si ypur height?"))
bmi = weight / (height ** 2)

if bmi < 18.5:
    obs = "are underweight"
elif bmi < 25:
    obs = "have a normal weight"
elif bmi < 30:
    obs = "are slightly overweight"
elif bmi < 35:
    obs = "are obese"
else:
    obs = "are clinically obese"
print(f"Your BMI is {bmi}, You {obs}.")

height = int(input("what is your height?"))  # must convert to int not str to compare with a number
price = 0
if height >= 120:
    print("can ride")
    age = int(input("How old are you?"))
    if age < 12:
        price += 5
        print(f"Your cost is {price}$")
    elif age <= 18:
        price += 7
        print(f"Your cost is {price}$")
    else:
        price += 12
        print(f"Your cost is {price}$")

    photo = input("Do you want to take a photo?")
    if photo == "y":
        price += 3
    print(f"Your total is {price}$")
else:
    print("can't ride")


print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")


height = int(input("what is your height?"))  # must convert to int not str to compare with a number
price = 0
if height >= 120:
    print("can ride")
    age = int(input("How old are you?"))
    if age < 12:
        price += 5
        print(f"Your cost is {price}$")
    elif age <= 18:
        price += 7
        print(f"Your cost is {price}$")
    elif age >= 45 & age <= 55:
        price = 0
    else:
        price += 12
        print(f"Your cost is {price}$")

    photo = input("Do you want to take a photo?")
    if photo == "y":
        price += 3
    print(f"Your total is {price}$")
else:
    print("can't ride")

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
score_true = 0
score_love = 0
full_name = name1.lower() + name2.lower()  # .lower() to make the str in lower case
score_true += full_name.count('t')         # .count() to count the element inside the() with the variable assigned to
score_true += full_name.count('r')
score_true += full_name.count('u')
score_true += full_name.count('e')
score_love = full_name.count('l') + full_name.count('o') + full_name.count('v') + full_name.count('e')

total_score = int(str(score_true) + str(score_love))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

# Leab year
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")
# OR
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

##########   PROJECT: TREASURE GAME ##########

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("You're at across road. where do you want to go? \"left\" or \"right\" \t")

if left_right.lower() == "left":
    print("You fall from a mountain. GAME OVER")
else:
    swim_ship = input("Yo found lake, \"swim\" or take a \"ship\"")
    if swim_ship.lower() == "ship":
        print("It was a pirate ship!!!! GAME OVER")
    else:
        door = input("You found a door, which door you want to take? \"Red\", \"BLue\", \"Yellow\" or \"Nothing\"")
        if door.lower() == 'yellow' or door == 'red':
            print('You\'re burned, GAME OVER')
        else:
            print("YOU WIN!")
