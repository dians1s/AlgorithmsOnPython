def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n - 1)


# Числа фибоначчи - 1,1,2,3,5,8,13,21


def fibonachi(n):
    if (n < 3):
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(8))
