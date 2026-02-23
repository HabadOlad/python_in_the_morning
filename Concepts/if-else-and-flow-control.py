#Flow control statements can decide which Python instructions to execute under which conditions.

'''
While the integer, floating-point, and string data types have an unlimited number of possible values,
the Boolean data type has only two values: True and False. 
'''

#When entered as Python code, the Boolean values True and False lack the quotation marks you place around strings, and they always start with a capital T or F, with the rest of the word in lowercase. 

'''
you can use Boolean values in expressions and store them in variables ❶.
If you don’t use the proper case ❷ or if you try to use True and False for variable names ❸, 
Python will give you an error message.

'''

'''
Flow control statements often start with a part called the condition and 
are always followed by a block of code called the clause.
'''

# condition is just a more specific name in the context of flow control statements. A condition always evaluates to a Boolean value, True or False. 

username = 'Mary'
password = 'swordfish'
if username == 'Mary':
   print('Hello, Mary')
if password == input('>'):
        print('Access granted.')
else:
        print('Wrong password.')

'''
if
The most common type of flow control statement is the if statement.
 An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. 
 The clause is skipped if the condition is False.

In plain English, an if statement could be read as, “If this condition is true, execute the code in the clause.” 
In Python, an if statement consists of the following:

The if keyword
A condition (that is, an expression that evaluates to True or False)
A colon
Starting on the next line, an indented block of code (called the if clause or if block)
'''

'''
else
An if clause can optionally be followed by an else statement.
 The else clause is executed only when the if statement’s condition is False. 
 In plain English, an else statement could be read as, 
 “If this condition is true, execute this code. 
 Or else, execute that code.” An else statement doesn’t have a condition, and in code, an else statement always consists of the following:

The else keyword
A colon
Starting on the next line, an indented block of code (called the else clause or else block)
'''

name = 'Alice'
if name == input(">"):
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

'''
elif
You would use if or else when you want only one of the clauses to execute. 
But you may have a case where you want one of many possible clauses to execute.
 The elif statement is an “else if” statement that always follows an if or another elif statement. 
 It provides another condition that is checked only if all of the previous conditions were False. 
 In code, an elif statement always consists of the following:

The elif keyword
A condition (that is, an expression that evaluates to True or False)
A colon
Starting on the next line, an indented block of code (called the elif clause or elif block)

'''

name = input(">")
age = input(">")
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')


name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')