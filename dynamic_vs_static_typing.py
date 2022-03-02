#python is a dynamically typed programming language, 
#in contrast to other langauges that are statically typed(C++, Java)
#to make it make sense, in Java, you would need to declare the type of data that will be stored in a variable

#Here is setting a variable in a statically typed language (java, C++)
#int score 

#in python, we don't need to do that, we simply assign the type value we want to assign the variable
#which is then "tranlated" in the background as to what the "data type" of that variable is

#here is a example with a interger data type assigning it to a variable
score = 10
print(type(score))

#Here is a another example with a string data type assigning it to variable
name = "Ghostface Killa"
print(name)
print(type(name))

#here is one last data type just to help it make sense
#here is a floating int data type (variable with numbers after the decimal point)
#For my case as a network engineer, i can only image how hard it would be to declare the data type each time 
#i wanted to write a description for an interace, for an IP address, etc!
pi = 3.14
print(type(pi))