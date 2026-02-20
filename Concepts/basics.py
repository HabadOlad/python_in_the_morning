#basics !
#this is a comment!
''''
This is a multi line comment
'''
#This is a program that says hello and asks for your name


print((10 * "-") + "program begins" + (10 * "-"))
print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
print("where are you from?")
location = input('>')
print('It is good to meet you, ' + my_name)
print("You're from " + location + " How exotic!")
print('The length of your name is:')
print(len(my_name))
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.') #string conversion into an age
print((10 * "-") + "program ends" + (10 * "-"))