def factorial(n):
    f = 1
    for i in range(2, n + 1):
            f = f * i
    return f
num = int(input("Introduce un número:"))
fact = factorial(num)
print (fact)