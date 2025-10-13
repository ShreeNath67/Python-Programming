"""
Pattern 6: Floyd's Triangle

1  
2 3  
4 5 6  
7 8 9 10  

Logic: Print a running counter num for i numbers in each row.
"""

num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()