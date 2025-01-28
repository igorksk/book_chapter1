def concatenate_numbers(numbers):
    # Convert each number to a string and join them together
    concatenated = ''.join(map(str, numbers))
    return int(concatenated)  # Convert the result back to an integer

# Input from the user
try:
    user_input = input("Enter a list of numbers separated by spaces: ")
    # Split the input into a list of integers
    numbers = list(map(int, user_input.split()))
    
    result = concatenate_numbers(numbers)
    print(f"Concatenated number: {result}")
except ValueError:
    print("Please enter a valid list of numbers.")
