"""Example: 
Enter size of triangle: 5
* * * * *
* * * *
* * *
* *
*
"""

n = int(input("Enter size of triangle: "))
for i in range(n, 0, -1):
    print("*" * i, end="")
    print()