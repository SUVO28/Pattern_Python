n = int(input("Enter a number: "))

for i in range(n+1):
    for j in range(n-1-i):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

# Enter a number: 5
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

