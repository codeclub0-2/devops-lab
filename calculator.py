import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division = Not possible (divide by zero)")
