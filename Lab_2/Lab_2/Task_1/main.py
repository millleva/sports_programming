def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Введіть значення n: "))

if n <= 12:
    print("n повинно бути більше 12.")
else:
    result = factorial(n)
    print(f"{n}! = {result}")