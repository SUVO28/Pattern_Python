n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

# Output-
# Enter a number: 5
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
