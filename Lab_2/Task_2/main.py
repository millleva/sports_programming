def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

factorial_100 = factorial(100)
power_100 = power(2, 100)

result = factorial_100 + power_100
print(f"Результат: {result}")
