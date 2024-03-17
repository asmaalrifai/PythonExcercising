#  RANDOMISATION AND PYTHON LISTS
import random

# random_integer = random.randint(0, 100)
# choice = int(input("write a number \t"))
#
# while random_integer != choice:
#     if random_integer < choice:
#         choice = int(input("choice is large"))
#     elif random_integer > choice:
#         choice = int(input("choice is small"))
# print(f"you win, num is {random_integer}")

# # 1 - 10
# random_int = random.randint(1, 10)
# # 0.0000000 - 0.99999999
# random_float = random.random()
# # 0.0000 - 4.99999
# random_float *= 5
# print(random_float)
# # 1.000000 - 10.999999
# random_double = random_int + random_float
# print(random_double)

# # Write your code below this line 👇
# # Hint: Remember to import the random module first. 🎲
# import random
#
# coin = random.randint(0,1)
#
# if coin == 0:
#   print('Tails')
# elif coin==1:
#   print('Heads')

##### LISTS #######

# states_of_america = ["Delaware", "Pennsylvania",
#                      "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#                      "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
#                      "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]

# state = states_of_america[1]            # assign an item to a variable
# state2 = states_of_america[-1]          # start from the end: Hawaii
# states_of_america[1] = "Pencilvania"    # change the item
#
# states_of_america.append("AsmakiLand")  # adding an item to the list (last item)
#
# print(states_of_america)

# # You are going to write a program that will select a random name from a list of names.
# # The person selected will have to pay for everybody's food bill.
# names_string = "asma, omar, ahmed, alrifai"
# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
#
# num_name = len(names) -1
# ran = random.randint(0,num_name)
# print(f"{names[ran]} is going to buy the meal today!")


# states_of_america = ["Delaware", "Pennsylvania",
#                      "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#                      "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
#                      "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
# # print number of items -> 50. last item (Hawaii) is num 49 since it starts from 0
# print(len(states_of_america))
#
# num_of_stats = len(states_of_america)
# print(states_of_america[num_of_stats - 1])

# NESTED LISTS
# fruits = ["Strawberry", "Apple", "Grapes", "Cherries"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# # from item 0 the element 3 -> Cherries
# print(dirty_dozen[0][3])

# You are going to write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#
# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
#
# if position[0] == 'A' and position[1] == '1':
#     map[0][0] = 'X'
# elif position[0] == 'B' and position[1] == '1':
#     map[0][1] = 'X'
# elif position[0] == 'C' and position[1] == '1':
#     map[0][2] = 'X'
# elif position[0] == 'A' and position[1] == '2':
#     map[1][0] = 'X'
# elif position[0] == 'B' and position[1] == '2':
#     map[1][1] = 'X'
# elif position[0] == 'C' and position[1] == '2':
#     map[1][2] = 'X'
# elif position[0] == 'A' and position[1] == '3':
#     map[2][0] = 'X'
# elif position[0] == 'B' and position[1] == '3':
#     map[2][1] = 'X'
# elif position[0] == 'C' and position[1] == '3':
#     map[2][2] = 'X'
#
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")
#
# OR solve it easier this way
# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
# # Your code below
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
#
# print(f"{line1}\n{line2}\n{line3}")
#
# OR solve it easier this way
# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)       # .index() to get the number of item(index) the matches the text/num between the ()
# num_index = int(position[1]) - 1
# map[num_index][letter_index] = 'X'
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")


###### PROJECT: ROCK, PAPER, SCISSORS #########
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
ran = random.randint(0, 2)
game = [rock, paper, scissors]
if choose > 2 or choose < 0:
    print("Invalid Input")
else:
    player = game[choose]
    print(player)
    computer = game[ran]
    print("Computer Chose: ")
    print(computer)

    if (choose == 2 and ran == 0) or (choose < ran):
        print("You Lose")
    elif (choose > ran) or (choose == 0 and ran == 2):
        print("You Win")
    elif choose == ran:
        print("its a draw")
