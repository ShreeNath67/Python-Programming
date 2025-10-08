"""
if condition:
   statement
elif condition:
   statement

   OR

if condition:
   statement
elif condition:
   statement
else:
   statement    
"""

a = int(input("Enter Age : "))

if a >= 18 and a < 120:
    print("You can vote.")

elif a < 0:
    print("Invalid Age.")

else:
    print("You can't vote.")