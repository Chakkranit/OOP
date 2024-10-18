rows = int(input("Enter number of rows: "))

cols = rows

print("Pattern 1:")
for i in range(rows):
    for j in range(cols):
        if j <= i:  
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  

print("\nPattern 2:")
for i in range(rows):
    for j in range(cols - i):
        print("*", end=" ")
    print()  

print("\nPattern 3:")
for i in range(rows, 0, -1):
    for _ in range(i - 1):
        print(" ", end="")
    for j in range(rows - i + 1):
        if j < rows - i:
            print("* ", end="")
        else:
            print("*", end="")
    print()

print("\nPattern 4:")
for i in range(rows, 0, -1):
    for _ in range(rows - i):
        print(" ", end="")
    for j in range(i):
        if j < i - 1:
            print("* ", end="")
        else:
            print("*", end="")
    print()

print("\nPattern 5:")
for i in range(rows):
    for j in range(rows):
        if j < rows - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()