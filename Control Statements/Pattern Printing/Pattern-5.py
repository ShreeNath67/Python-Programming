"""
Pattern 5: Repeated Row Number

1  
2 2  
3 3 3  
4 4 4 4  

Logic: Print number i exactly i times in row i.
"""

for i in range(1,5):
    for j in range(1,i+1):
        print(i, end=" ")
    print()