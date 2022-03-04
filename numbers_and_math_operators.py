#Numbers and Math Operators session
#python numbers: intergers, floats and complex

#Arithmic operators - Used to perform common math operations
#--------------------------

#addition = +
additionEx = 5 + 6
print(additionEx)

#subtraction = -
subtractionEx = 6 - 5
print(subtractionEx)

#division = /
divisionEx = 15 / 3
print(divisionEx)

#floor or interger division = //
floorAndintergerdivisionEx = 15 // 3
print(floorAndintergerdivisionEx)

#multiplication = *
multiplicationEx = 3 * 5
print(multiplicationEx)

#exponentiation or raising to a power = **
exponetiationEx = 2 ** 6
print(exponetiationEx)

#modulus (mod) = %
modulusEx = 15 % 3
print(modulusEx)

#Assigment Operators
#-------------------------

#simple assignment = "="
a = 1
a = a + 1
print(a)

#increment assignment = "+="
a += 5
print(a)

#decrement assignment = "-="
a -= 6
a -= 7
print(a)

#multiplication assignment = "*=" 
a *= 5
a *= 1
print(a)

#division assignment = "/="
a /= 5
print(a)

#power assignment = "**="
b = 2
b **= 4
print(b)

#modulus assignment = "%="

#floor division assignment = "//="
c = 15
c //= 3
print(c)

#Built-in functions for math operations
#---------------------------

#divmod() - finds the result and remainder at the same time
print(divmod(15, 4))
print(15 // 4)

#pow() - it gives us the value of the "x" to the power of "y"
print(pow(2,10))
print(10 ** 10)

#round() - rounds a number to a certain decimal point
print(18 / 13)
print(round(18/13, 3))

d = 1.23456789
print(round(d,4))

#sum() - it will calculate a sum
numbers = [1, 5, 66, 100]
print(sum(numbers))

#max() - returns the max value for a list of values(highest value)
print(max(4, 2, 1000, 55, -1)
)
#min() - returns the min value for a list of values (lowest value)
print(min(-7, -4, -10, 500))