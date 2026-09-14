def check_even_or_odd(number):
    return number % 2 == 0

user_number = int(input("Enter a number to check if it is even or odd:"))
result = check_even_or_odd(user_number)
if result is True:
    print(f"{user_number} is an even number.")
else:
    print(f"{user_number} is an odd number.")