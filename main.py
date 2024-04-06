#
#"Title Screen"
print("Welcome to Theodore's calculator\n1.- Choose two Numbers\n2.- Choose an Operation")
#Log numbers
num1 = input("\nFirst Number: ")
num1 = float(num1)
num2 = input("\nSecond Number: ")
num2 = float(num2)
#Get operation
operation = input("Please enter any of the following operations\nAddition\nSubtraction\nMultiplication\n> ")
#Initialize if else loop
if operation == "Addition": 
    output = num1 + num2
    print(f"Your number is {output}")
elif operation == "Subtraction": 
    output = num1 - num2
    print(f"Your number is {output}")
elif operation == "Multiplication": 
    output = num1 * num2
    print(f"Your number is {output}")
else:
    print("Please choose a valid operation")