pattern = int(input("Enter the size of the pattern"))
counter = pattern
while counter > 0:
    for items in range(pattern):
        print("*", end = "")
    print()
counter -= 1