user_number_1 = int(input("Insert the first number: "))
user_number_2 = int(input("Insert the second number: "))
# user_number_1 and user_number_2 are the two numbers the user inputs to perform calculations.``
calc_symbol = input("Enter the calculation symbol to be used (+, -, *, /): ")
if calc_symbol == "+":
    calc_sum = user_number_1 + user_number_2
    print(f"The sum of {user_number_1} + {user_number_2} is {calc_sum}.")
elif calc_symbol == "-":
    calc_difference = user_number_1 - user_number_2
    print(f"The difference of {user_number_1} - {user_number_2} is {calc_difference}.")
elif calc_symbol == "*":
    calc_product = user_number_1 * user_number_2
    print(f"The product of {user_number_1} * {user_number_2} is {calc_product}.")
elif calc_symbol == "/":
    if user_number_2 == 0: # For division we guard the denominator. Division fails only when the denominator is zero.(You can't divide by zero). The numerator can be 0/2 not 2/0. Hence the need to check if user_number_2 is zero before performing the division operation.
        print("Error: Division by zero is not allowed.")
    else:
        calc_quotient = user_number_1 // user_number_2
        calc_remainder = user_number_1 % user_number_2
        print(f"The quotient of {user_number_1} // {user_number_2} is {calc_quotient}")
        if calc_remainder == 0:
            print(f"{user_number_1} is divisible by {user_number_2}.")
        else:
            print(f"The remainder is {calc_remainder}.")
else:
    print("Error: Invalid calculation symbol. Please use +, -, *, or /.")

#Because calc_symbol holds what the user types. Users normally enter / to mean “divide”; // is a Python operator meaning integer (floor) division, not a common user input.
#use // for an integer quotient and % for the remainder; use / when you want a (possibly fractional) result(basically a float).
# TRY WITH FLOATS LATER ON AND SEE:Why tolerance is needed: floating-point numbers are approximations, so calculations can leave tiny errors. Example:

#0.1 + 0.2 == 0.3 is False because (0.1 + 0.2) - 0.3 equals about 5.55e-17, not exactly 0.0.
#What tolerance is: a small threshold (like 1e-9) used instead of exact equality. It means “treat values within this tiny distance of zero as zero.”  