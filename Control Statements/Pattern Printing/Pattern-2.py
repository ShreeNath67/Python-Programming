"""
Pattern 2: Right-Angled Triangle

*
**
***
****

Logic: Print i stars in row i.
"""

for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()