n = int(input("Enter a number: "))

for i in range(n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Output-
# Enter a number: 5
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
