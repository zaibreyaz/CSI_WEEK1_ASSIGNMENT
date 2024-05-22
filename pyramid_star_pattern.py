"""Example: 
Enter size of pyramid: 5
    *
   * *
  * * *
 * * * *
* * * * *

"""

n = int(input("Enter size of pyramid: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* " * i, end="")
    print()