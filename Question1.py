# Number of rows
rows = 5

# Loop to increase the number of stars
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Loop to decrease the number of stars
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
