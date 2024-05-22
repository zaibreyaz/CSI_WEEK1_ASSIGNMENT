"""Example: 
Enter size of triangle: 5
*
* *
* * *
* * * *
* * * * * 
"""

n = int(input("Enter size of triangle: "))
for i in range(1, n+1):
    print("*" * i, end="")
    print()