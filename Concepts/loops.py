'''
while Loop Statements
You can make a block of code execute over and over again using a while statement. The code in a while clause will be executed as long as the statement’s condition is True. In code, a while statement always consists of the following:

The while keyword
A condition (that is, an expression that evaluates to True or False)
A colon
Starting on the next line, an indented block of code (called the while clause or while block)

'''

spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

#compare this to this which uses a while statement

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1