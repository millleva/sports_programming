def fastPower(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        halfPower = fastPower(a, n // 2)
        return halfPower * halfPower
    else:
        halfPower = fastPower(a, (n - 1) // 2)
        return halfPower * halfPower * a

a = 3
n = 10
result = fastPower(a, n)
print(f"{a} в ступені {n} дорівнює {result}")
