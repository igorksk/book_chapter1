def count_digits(number):
    # Convert the number to a string to iterate through digits
    number_str = str(abs(number))  # Handle negative numbers by taking the absolute value
    
    # Create a dictionary to store the count of each digit
    digit_count = {str(i): 0 for i in range(10)}
    
    # Count occurrences of each digit
    for digit in number_str:
        digit_count[digit] += 1
    
    return digit_count

# Input from user
try:
    user_input = int(input("Enter a number: "))
    result = count_digits(user_input)
    
    print("\nDigit counts:")
    for digit, count in result.items():
        print(f"{digit}: {count}")
except ValueError:
    print("Please enter a valid integer.")
