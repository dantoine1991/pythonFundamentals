# User Input

# The input() function is used to get information from the user running the program
print('An example if using the input() function')

# Here i am declaring a variable as the input function
name = input()

# Here I am using the type() and print() function display the 
# data type of the Variable and to print a string requesting input from 
# from the user
print("Type:", type(name))
print("Your name is:", name)


# Here is another example of using the input() function but this time I am using 
# a math operator to assign the sum to a variable 
price = input('Enter the price:')
quantity = input("Enter the quantity:")

# total_value = price * quantity --> This will not work because you cannot 
# do math functions with a string, 

# To make it work, we need to convert the type to a int
total_value = int(price) * int(quantity)

# Now, the print function will print a string and the variable 'total_value'
print('Total value:', total_value)
