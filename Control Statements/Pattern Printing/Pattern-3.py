"""
Pattern 3: Inverted Triangle

****
***
**
*

Logic: Print n - i + 1 stars in row i.
"""

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()