# Assignment 1 and 2 
# Write Program that accept two number from user add print 
# Addition , Substraction, Multiplication & Division

firstNumber = int(input("Enter first number"))
secondNumber = int(input("Enter second number"))

addition = firstNumber + secondNumber
print("Addition: ", addition)

substration = firstNumber - secondNumber
print("Substraction: ", substration)

multiplication = firstNumber * secondNumber
print("Multiplication: ", multiplication)

division = firstNumber // secondNumber
print("Division: ", division)

# Write program to take username and age and display

name = input("Enter your name")
age = int(input("Enter your age"))

print(f"Hello {name}, you will turn {age+1} next year.")