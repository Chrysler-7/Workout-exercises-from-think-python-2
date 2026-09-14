choose_temp_converter = input("Choose the temperature converter (C to F or F to C): ").strip().lower()
# strip() removes extra spaces at the beginning and end. " c to f " becomes "c to f" and " F to C " becomes "f to c". lower() converts the input to lowercase, so "C TO F" becomes "c to f" and "F TO C" becomes "f to c". This makes the input case-insensitive and more user-friendly.
# lower() converts the input to lowercase, so "C TO F" becomes "c to f" and "F TO C" becomes "f to c". This makes the input case-insensitive and more user-friendly.
if choose_temp_converter in {"c to f", "celsius to fahrenheit"}:
    celsius_temp = float(input("Enter the temperature value in Celsius: "))
    fahrenheit_result = (celsius_temp * 9 / 5) + 32
    print(f"The temperature value in Fahrenheit is: {fahrenheit_result:.2f}")

elif choose_temp_converter in {"f to c", "fahrenheit to celsius"}:
    fahrenheit_temp = float(input("Enter the temperature value in Fahrenheit: "))
    celsius_result = (fahrenheit_temp - 32) * 5 / 9
    print(f"The temperature value in Celsius is: {celsius_result:.2f}°C")

else:
    print("Error: Invalid temperature converter choice.")

    #Revisit and make more improvements to the code where i can
    # celcius to fahrenheit formula: (C * 9/5) + 32
    # fahrenheit to celcius formula: (F - 32) * 5/9