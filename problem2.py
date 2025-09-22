print("Problem 2: Series of odd numbers")
x = int(input("Enter a number: "))
i = 1
count = 0
while count < x:
    print(i, end=", " if count < x-1 else "\n")
    i += 2
    count += 1