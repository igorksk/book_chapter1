def transform_number(number):
    # Convert the number to a string to process each digit
    number_str = str(abs(number))  # Handle negative numbers by taking the absolute value
    
    # Transform each digit to 9 - digit
    transformed_digits = ''.join(str(9 - int(digit)) for digit in number_str)
    
    # Preserve the original sign of the number
    return int(transformed_digits) if number >= 0 else -int(transformed_digits)

# Input from the user
try:
    user_input = int(input("Enter a number: "))
    result = transform_number(user_input)
    print(f"Transformed number: {result}")
except ValueError:
    print("Please enter a valid integer.")
