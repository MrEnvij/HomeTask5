from utils import factorial

result = factorial(5)
print(f"Факторіал числа 5 дорівнює: {result}")

from utils import is_prime

print(is_prime(17)) 

from utils import is_power_of_five

numbers = [1, 5, 25, 125, 7, 10, 625]
for num in numbers:
    if is_power_of_five(num):
        print(f"{num} є степенем 5.")
    else:
        print(f"{num} не є степенем 5.")

from utils import is_power_of_two

numbers = [1, 2, 4, 8, 16, 3, 5, 10, 32]  # 1 = 2^0, 2 = 2^1, 4 = 2^2, 8 = 2^3, 16 = 2^4, 32 = 2^5
for num in numbers:
    if is_power_of_two(num):
        print(f"{num} є степенем 2.")
    else:
        print(f"{num} не є степенем 2.")
