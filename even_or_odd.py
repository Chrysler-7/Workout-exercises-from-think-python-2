def check_even_or_odd(number):
    if number % 2 == 0: #Basically the modulo operator shows only the remainder not the quotient e.g 0
        return True
    else:
        return False
user_number = int(input("Enter a number to check it it is even or odd:"))
result = check_even_or_odd(user_number) #This is where we call the function and pass in the user input.
if result is True:
    print(f"{user_number} is an even number.")
else:
    print(f"{user_number} is an odd number.")



