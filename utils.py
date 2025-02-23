def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

def is_power_of_five(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    while n > 1:
        if n % 5 != 0:
            return False
        n //= 5
    return True

def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    while n > 1:
        if n % 2 != 0:
            return Fals
        n //= 2
    return True

