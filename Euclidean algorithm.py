a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    while b > 0:
        a, b = b, a % b
elif b > a:
    a, b = b, a
    while b > 0:
        a, b = b, a % b
print("GCD =", a)
