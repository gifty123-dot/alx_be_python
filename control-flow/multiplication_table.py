number = int(input("Enter a number to see its multiplication table: "))

for multiplier in range(1, 10):
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")
