# Automation onboarding
# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…

def fibonacci(maxN):
    total = 0
    firstN = 0
    secondN = 0
    print(total)
    while total < maxN:
        total = firstN + secondN
        if total > maxN:
            break
        else:
            print(total)
            firstN = secondN
            if secondN == 0:
                secondN = 1
            else:
                secondN = total


fibonacci(150)
