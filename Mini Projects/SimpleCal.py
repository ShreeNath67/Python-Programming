"""
Can perform simple calculations.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = input("Choose from these: (+, -, *, /, //, %, ** ): ")

if choice == "+" :
    print(f'Result is: {a+b}')

elif choice == "-":
    print(f'Result is: {a-b}')

elif choice == "*":
    print(f'Result is: {a*b}')  

elif choice == "/":
    print(f'Result is: {a/b}') 

elif choice == "//":
    print(f'Result is: {a//b}') 

elif choice == "**":
    print(f'Result is: {a**b}')

else:
    print("Invalid Choice.")

   