# DATA TYPE

num_char = str(len(input("whats is your name")))

# or i can use it in another variable
# new_num_char = str(num_char)

print("Your name has "+ num_char + " characters")

# it is not like the previous one:
name =input("Whats is ur name\n")
print(len(name))    #-> or print(len(input()))

a = float(123)
print(a + "  " + type(a))

print(70 + float("100.5"))  #-> works output is 170.5
print(str(70)+str(100))     #-> works output 70100
print(70 + float("100.5t")) #-> Error because of the letter


# Practice
# Write a program that adds the
# digits in a 2 digit number.
# e.g. if the input was 35, then the
# output should be 3 + 5 = 8

two_digit_number = input()   #-> str
a = int(two_digit_number)
a1 = int(a/10)
b = int(a%10)
print(a1 + b)

a= int(two_digit_number/10)    #-> Error data type

# Another Solution:   -> using string []
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)

# MATHMATICAL OPERATIONS

# in division, it gives 'float' number
print(2**6)   #-> 2^6 power

print(3 * 3 + 3 / 3 - 3)
# make the answer ti be 3
print(3 * (3 + 3) / 3 - 3)

# Practice
# Write a program that calculates the
# Body Mass Index (BMI) from a user's
# weight and height.
BMI = w / (h^2)

height = input()
weight = input()
float_height = float(height)
float_weight = float(weight)
print(int(float_weight / (float_height**2)))

# Another Solution
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

print(8 / 3)            #-> 2.66666665
print(int(8 / 3))       #-> 2
print(round(8 / 3))     #-> 3
print(round(8 / 3, 2))  #-> 2.67
print(round(2.6666, 2))  #-> 2.67

print(type(8/4))     #->  float (always)
print(type(8//4))    #-> int

score=2
print("your score is "+score)   #-> Error diff data types, all should be str
print("your score is " + str(score))  #-> works, all str

# also use f-String
print(f"your score is {score}")   #-> f"" do all the converting

# Practice
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.

age = input()
weeks = int(age) * 52
left = 4680 - weeks
print(f"You have {left} weeks left.")

# Another Solution
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")

name = input("whatrs ur name? ")
print(f"hello, {name}")          #-> works

name = input("whatrs ur name? ")
print("hello, " + name)          #-> works, same data type str

age = 12
print(f"ure {age} y/o")         #-> works using f-String

age = 12
print("ure " + age)             #-> Error diff data types

########### DAY'S PROJECT #################
########### Tip Calculator #################
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = (int(input("What percentage tip would you like to give? 10, 12, or 15? ")))  # i can put the tip/100 here but i wanna save the data
people = int(input("How many people to split the bill? "))

bill_with_tip = bill + bill*tip/100      # another variable to save the bill data
each_person = bill_with_tip / people
#final_amount = round(each_person, 2)       # will not round to 2 if the number has only 1 decimal digit
final_amount = "{:.2f}".format(each_person) # will round to 2 decimal digit every time

print(f"Each person should pay: {final_amount}")

