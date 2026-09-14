import random
#validation of input

def get_valid_integer(prompt):
    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value <= 0:
            print("Please enter a number greater than zero.")
            continue

        return value
    
# Accepts only whole numbers
# rejects decimals like int("3.5") and strings like int("abc")
# rejects 0 and negatives
# keeps asking until the user enters a valid value
# if statements are for checking known vaues while try is for handling unexpexted errors and the program does sth else instead of crashing.
# try uses: converting user input, reading files,dividing by numbers that might be zero, anything that might fail.
#IN SIMPLE TERMS: ->IF/ELSE/ELIF- FOR LOGIC,TRY/EXCEPT- FOR ERROR HANDLING,WHILE- FOR REPETITION AND RISKY OPERATIONS THAT MAY FAIL.

#Returns one random result
def roll_die(sides):
    return random.randint(1, sides)

#Accepts number of sides
#Generates a random number between 1 and sides
#Returns it

#Collects multiple results
def roll_multiple_dice(number_of_dice, sides):
    rolls = []
    for i in range(number_of_dice):
        rolls.append(roll_die(sides))
    return rolls

# Creates an empty list called rolls that stores individual dice rolls
# Rolls once per die and appends the result to rolls(the list)
# Returns the list of rolls

#Validates yes/no input
def ask_to_continue():
    while True:
        answer = input("Do you want to roll again? (yes/no): ").strip().lower()
    
        if answer in ("no", "n"):
            return False
        elif answer in ("yes", "y"):
            return True
        else:

          print("Invalid input. Please enter 'yes' or 'no'.")

#MAIN LOOP: ROLLS,PRINTS AND REPEATS UNTIL THE USER EXITS
while True:
    dice_count = get_valid_integer("Enter the number of dice to roll: ")
    sides = get_valid_integer("Enter the number of sides on each die: ")

    rolls = roll_multiple_dice(dice_count, sides)
    total = sum(rolls)

    print("Dice rolled:",rolls)
    print("Total:", total)

    if not ask_to_continue():
        print("Thanks for playing!")
        break


#the yes/no question is validated properly
#invalid input does not break the loop
#clean separation of responsibilities
#easier to read and maintain


#break and continue are used to control the flow of the loop. break exits the loop entirely, while continue skips the rest of the current iteration and moves on to the next one.
#break and continue are used only in a loop e.g while True: or for...in...:, while return is used in a function to exit the function and optionally return a value.

#validates positive whole numbers
#rolls one or more dice
#stores the results in a list
#calculates the total
#asks the user if they want to roll again
#stops when the user says no
#accepts uppercase input like YES / NO