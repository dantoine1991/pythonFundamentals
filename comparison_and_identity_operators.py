#Comparison Operators
#-----------------------------

#"==" - Equal to (equality) - compares two values and returns "True" or "False"
print("Is 2 equal to 2?")
print(2 == 2) #this should give a value of True since 2 is equal to 2
print("Is 5 equal to 6?")
print(5 == 6) #This should give a value of False since 5 is not equal to 6

#"!=" - Not equal to (inequality)
print("Is 2 not equal to 2?")
print(2 != 2) #this should give a value of False since 2 is equal to 2
print("Is 5 not equal to 6?")
print(5 != 6) #this should give a value of True since 5 is not equal to 6

#">" - Greater than
print("Is 2 greater than to 2?")
print(2 > 2) #This should give a value of False since 2 is not greater than 2
print("Is 5 greater than to 6?")
print(5 > 6) #This should give a value of False since 5 is not greater than 6

#">=" - Greater than or equal to
print("Is 2 greater than OR equal to 2?")
print(2 >= 2) #This should give a value of True since 2 is not greater than 2 but is equal to 2
print("Is 5 greater than OR equal to 6")
print(5 >= 6) #This should give a value of False since 5 isnt greater than 6 nore equal

#"<" - Less than
print("Is 2 less than to 2?")
print(2 < 2) #this should give a value of False since 2 is not less than 2
print("Is 5 less than to 6?")
print(5 < 6) #This should give a value of True since 5 is less than 6

#"<=" - Less than or equal to
print("Is 2 less than OR equal to 2?")
print(2 <= 2) #this should give a value of True since 2 is not less than 2 but equal to 2
print("Is 5 less than OR equal to 6?")
print(5 <= 6) #This should give a value of True since 5 is less than 6 and not equal to 6

#Identity Operators - they compare the memory values of the variable, not the value of the variable
#---------------------------

#is 
a = 1
b = 2
print(id(a))
print(id(b))
print("Is the memory location value of 'a' equal to 'b'?")
print(a is b) #This should give a value of False since 'a' doesnt have the same memory id number of 'b'

#is not
a = 1
b = 2
print(id(a))
print(id(b))
print("Is the memory location value of 'a' not equal to 'b'?")
print(a is not b) #This should give a value of True since 'a' doesnt have the same memory id number of 'b'

#NOTE - Immutable variables: integers, floats, strings, tuples, FrozedSets
#NOTE - Mutable variables: list, sets and dictionaries

#Logical Operators
#----------------------------
#and
#or
#not

#Membership Operators
#----------------------------
#in
#not in

