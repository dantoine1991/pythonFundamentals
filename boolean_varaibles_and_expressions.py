# Boolean Variables and Expressions

# A boolean variable is an object of the bool class which is an int or interger subclass
print(bool(1))

# In python there are 2 boolean constants defined: True and False
# True is interpreted as the interger 1 and False as interger 0
print(bool(1))
print(bool(0))

    # There are 3 boolean or logical operators in Python: "and", "or", and "not"


# Another constant is 'None' that is frequently used to represent the absence of a value

# Truthfulness of Objects

# Object Type                       | Bool(obj)
# ---------------------------------------------
# int                               | bool(0) is False, bool(x) is True if (x != 0)
x = 1
if x == 1:
    print("True")
else:
    print("False")

x = 0
if x == 1:
    print("True")
else:
    print("False")

# ----------------------------------------------------------------------------------------
# float                             | bool(0,0) is False, bool(x) is True if (x != 0,0)
x = 1.0
if x == 1.0:
    print("True")
else:
    print("False")

x = 0.0
if x == 1.0:
    print("True")
else:
    print("False")

# -----------------------------------------------------------------------------------------
# Sequences(Strings, list, tuples)  | False if empty, True otherwise

x = ('Minato', 'Zoro', 'Gojo')
print("Here is an example of a tuple boolean returning True and False")
print(bool(x))

x = list()
print(bool(x))

x = "Deku"
print("Here is an example of a string boolean returning True and False")
print(bool(x))

x = ""
print(bool(x))


# -------------------------------------------------------------
# Dictionary, Set                   | False if empty, True otherwise
x = {"neo": "The 1"}
print("Here is an example of a dictionary boolean returning True and False")
print(bool(x))

x = dict()
print(bool(x))

# -------------------------------------------------------------
# Custom classes                    | They implement the __bool__and/or__lean methods


# The boolean "and" operator returns 'True' if both expressions are 'True.
    # If any expression is 'False' the entire expression is evaluated to 'False'
print("Here is an example of a the 'and' operator returning True and False")
if 8 < 10 and 9 < 10:
    print("True")
else:
    print("False")

if 10 < 8 and 9 < 10:
    print("True")
else:
    print("False")

# The boolean "or" operator returns 'True' if any operand is 'True'.
    # It will return 'False' only if both expressions evalute to 'False'
print("Here is an example of a the 'or' operator returning True and False")
if 10 < 8 or 9 < 10:
    print("True")
else:
    print("False")

if 10 < 8 or 10 < 9:
    print("True")
else:
    print("False")

# The "not" operator will simply negate the expression "true" value
print("Here is an example of a the 'not' operator returning False because if the value is true, the 'not' operator tells the boolean to ignore any comparasions that are true")
print(not 2 == 2)
print(not 5 == 5)

print("Here is an example of a the 'not' operator returning True because if the value is False, the 'not' operator sees the comparision as not being true already, so it returns true")
print(not 5 == 2)
print("Trippy right? LOL")