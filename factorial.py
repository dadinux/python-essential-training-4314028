def factorial(number):
    i = 1
    result = number
    while i < number:
        result = result * (number - i)
        i = i + 1
        print(result)



factorial(10)