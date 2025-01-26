def fibonacci(number):
    
    if number == 0:
        return number;

    elif number == 1:    
        return number;
    
    else:
        return fibonacci(number - 1) + fibonacci(number - 2);


number = int(input("Enter number: "))

nums = [fibonacci(k) for k in range(number)]

print(nums)
