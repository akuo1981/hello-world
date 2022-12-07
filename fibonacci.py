# Automation onboarding
# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…

def fibonacci(max_number):
    total = 0
    first_number = 0
    second_number = 0
    print(total)
    while total < max_number:
        total = first_number + second_number
        if total > max_number:
            break
        else:
            print(total)
            first_number = second_number
            if second_number == 0:
                second_number = 1
            else:
                second_number = total


fibonacci(150)
