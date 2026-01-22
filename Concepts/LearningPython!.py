#this is a comment in python

'''
This is a multi line comment in python ,

although technically they are string literals,

but can be used as comments if they are not assigned to a variable

'''

'''
In fact, it’s now fairly safe to say that Python
 played a pivotal role in changing the world. 
 By spearheading a shift from statically typed compiled languages to dynamically typed scripting languages, 
 Python ushered in changes that were at least as profound as those of the earlier transition from 
 machine language to compiled languages. 

 
'''

'''
Compiled Languages: In a compiled language, the entire
source code is translated into machine code by a
program called a compiler before the program is 
run. This results in a standalone executable file
(like an .exe on Windows).Workflow: Code $\rightarrow$ Compiler $\rightarrow$ Executable File $\rightarrow$ Output.
Performance: Generally much faster because the translation is done once, and the computer runs the pre-optimized machine code directly.
Error Detection: Errors are caught during the "build" phase. 
If there is a syntax error, the program won't even finish compiling.Examples: C, C++, Rust, Go, Swift.
'''

'''
Interpreted Languages
In an interpreted language, 
the source code is not translated all at once. Instead, 
a program called an interpreter reads and executes the code 
line-by-line, on the fly, as the program is running.Workflow: Code $\rightarrow$ Interpreter $\rightarrow$ Output.
Performance: Typically slower because the computer has to translate each line of code every time it runs.
Error Detection: Errors are caught at "runtime." The program will start running and only crash when it hits the specific 
line containing the error.
Examples: Python, JavaScript, Ruby, PHP.
'''

'''
On a related note, people also sometimes call Python an interpreted language to distinguish it from languages like C and C++. While this is also sometimes meant to pigeonhole, it’s also easier to dismiss: there are many implementations of Python today, spanning the spectrum from traditional interpreters to traditional compilers, so “interpreted” doesn’t apply. The clearer distinction may be that Python is dynamically typed, not statically typed like languages that are normally compiled. As you’ll soon learn, this accounts for much of the power that Python brings to development tasks

In a dynamically typed language, the variable doesn't have a fixed type—only the value it holds does. You don't have to declare if a variable is a string or an integer; the computer figures it out while the program is running

A loosely typed language is "forgiving." If you try to perform an operation on two different types (like adding a number to a string), the language will try to automatically convert (coerce) one of them so the code doesn't crash.

The opposite of a dynamically typed language is a statically typed language.

While dynamic languages check types while the program is running, static languages check types while the program is being compiled (before it ever starts).
'''