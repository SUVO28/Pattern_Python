n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(n + 1 - i):
        print(i, end=" ")
    print()

# Output-
# Enter a number: 5
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

