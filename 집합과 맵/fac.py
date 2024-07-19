def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n - 1)
    else:
        return 1


q = my_factorial(11) * my_factorial(2)
e = my_factorial(13)
result = e / q

print(result)
