# Loops
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)


# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# tot = 0
# for height in student_heights:
#     tot += height
#
# num_of_students = 0
# for students in student_heights:
#     num_of_students += 1
# average_height = round(tot / num_of_students)
# print(f"total height = {tot}")
# print(f"number of students = {num_of_students}")
# print(f"average height = {average_height}")


# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# high = 0
# for grade in student_scores:
#     if high < grade:
#         high = grade
#
# print(f"The highest score in the class is: {high}")


# for number in range(0, 10):     # doesnt include 10
#     print(number)
#
# for number in range(1, 10, 3):  # 3 is the step, 3 steps after the first item
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# target = int(input())  # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
# total = 0
# for number in range(2, target + 1):           # all the even numbers
#     if number % 2 == 0:
#         total += number
#
# print(total)


# for num in range(1, 101):
#     if (num % 5 == 0) and (num % 3 == 0):
#         print("FizzBuzz")
#         continue
#     elif num % 3 == 0:
#         print("Fizz")
#         continue
#     elif num % 5 == 0:
#         print("Buzz")
#         continue
#     print(num)
# OR
# for num in range(1, 101):
#     if (num % 5 == 0) and (num % 3 == 0):
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


###### PROJECT: CREATE A PASSWORD GENERATOR #######
import random

print("Welcome to make your password SAFE from now on")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_num = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# listed = [letters, numbers, symbols]
tot = letters + numbers + symbols

password = ""
for num in range(1, num_letters + 1):
    letter_ran = random.randint(0, 51)
    password += letters[letter_ran]
print(password)

for num in range(1, num_symbols + 1):
    symbol_ran = random.randint(0, 8)
    password += symbols[symbol_ran]
print(password)

for num in range(1, num_num + 1):
    num_ran = random.randint(0, 8)
    password += numbers[num_ran]
print(password)

new_password = ""
for num in range(0, len(password) - 1):
    rand_new_password = random.randint(0, len(password) - 1)
    new_password += password[rand_new_password]
print(new_password)

total = num_num + num_letters + num_symbols
password = ""
for pas in range(1, total + 1):
    random_pas = random.randint(0, 64)
    password += tot[random_pas]
print(password)

newList = []
for password in tot:
    rand_pass = random.randint(0, 70)
    newList += tot[rand_pass]

print("-------------------------------------")

# Easy way

password = ""

for char in range(1, num_letters + 1):
    password += random.choice(letters)

for sym in range(1, num_symbols + 1):
    password += random.choice(symbols)

for num in range(1, num_num + 1):
    password += random.choice(numbers)

print(password)

# Hard way
password_list = []

for char in range(1, num_letters):
    password_list.append(random.choice(letters))

for sym in range(1, num_symbols):
    password_list += random.choice(symbols)

for num in range(1, num_num):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(''.join(password_list))

# Or

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")
