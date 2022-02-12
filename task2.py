# create a reusable package for a calculator

import calculator
x,y = input("Enter two numbers : ")

Additon = calculator.add(x,y)
print(Additon)

Subtractin = calculator.subtract(x,y)
print(Subtractin)

Multiplication = calculator.multiply(x,y)
print(Multiplication)

Division = calculator.divide(x,y)
print(Division)
