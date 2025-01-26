def factorial(number):

    if number < 0:
        print("can't be negative")

    elif number == 0:
        return 1

    else:
        return number * factorial(number - 1)

number = int(input("Enter number: "))

nums = [factorial(k) for k in range(number)]

print(nums)

