"""
Pattern 8: Right-Aligned Triangle

    *  
   **  
  ***  
 ****  

Logic: Print n - i spaces followed by i stars in each row.
"""

n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(" ", end="")
        else:
            print("*", end="")
    print()
