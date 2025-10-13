"""
Pattern 4: Number Triangle

1  
12  
123  
1234  

Logic: Print numbers from 1 to i in row i.
"""

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print()