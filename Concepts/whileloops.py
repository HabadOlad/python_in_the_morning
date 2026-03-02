'''
while Loop Statements
You can make a block of code execute over and over again using a while statement. The code in a while clause will be executed as long as the statement’s condition is True. In code, a while statement always consists of the following:

The while keyword
A condition (that is, an expression that evaluates to True or False)
A colon
Starting on the next line, an indented block of code (called the while clause or while block)

'''

# spam = 0
# if spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

#compare this to this which uses a while statement

# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1

'''
The code with the if statement checks the condition, and it prints "Hello, world." 
only once if that condition is true. The code with the while loop, on the other hand,
 will print it five times. The loop stops after five prints because the integer in spam 
 increases by one at the end of each loop iteration, which means that the loop will
execute five times before spam < 5 is False.



'''

#break statements

while True:
    print('Please type your name.')
    name = input('>')
    if name == 'your name':
        break
print('Thank you!')