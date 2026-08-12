num = int(input("Enter a number: "))

# Sign check
if num == 0:
    print(f"{num} is zero.")
elif num > 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is negative.")

# Parity check
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")