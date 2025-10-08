"""  
Used to compare object identity (Memory Location)
"""  
a = [1, 2, 3]  
b = a  
c = [1, 2, 3]  

print(a is b)       # Same object  
print(a is not c)   # Different object  
