"""
Pattern 7: Reverse Number Triangle

5  
5 4  
5 4 3  
5 4 3 2  

Logic: Print numbers from n down to n - i + 1 in row i.
"""

for i in range(1,5):
    for j in range(5,5-i,-1):
        print(j, end=" ")
    print()