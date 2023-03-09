n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

# Output-
# Enter a number: 5
# * * * * *
# * * * *
# * * *
# * *
# *
