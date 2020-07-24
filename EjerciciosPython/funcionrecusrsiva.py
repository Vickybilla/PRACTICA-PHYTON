def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num - 1)
        return fact

    
mi_factorial = factorial(5)
print(mi_factorial)