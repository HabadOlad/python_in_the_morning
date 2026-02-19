'''
Part 1. Conditional statement
Question 1: Write a Python program that:
1.	Accepts four integer inputs from the user: a1, a2, a3, and a4.
2.	Determines which of the inputs is the greatest.
3.	Prints which variable holds the greatest value along with its value.
4.	If two or more numbers are equal and share the greatest value, indicate all variables with that greatest value.
Bonus: Add input validation to ensure that all entries are valid integers.
a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if a1 >= a2 and a1 >= a3 and a1 >= a4:
    print("Greatest number is a1:", a1)
elif a2 >= a1 and a2 >= a3 and a2 >= a4:
    print("Greatest number is a2:", a2)
elif a3 >= a1 and a3 >= a2 and a3 >= a4:
    print("Greatest number is a3:", a3)
else:
    print("Greatest number is a4:", a4)


'''

def 