# Author: Endri Dibra

"""
This is our Python/NLP course
Here we will learn the basics in order
to understand our final project
"""

"""
Firstly you should install Pycharm,
Python's IDE. Find how here:
https://www.jetbrains.com/help/pycharm/installation-guide.html
"""

"""now let's start programming !"""

# Your first Python Program
print("Hello World !")


# Python Variables and Data Types
x = 10
print("This is an integer: ",x)
print(type(x))

y = 12.0
print("This is a floating point number: ",y)
print(type(y))

letter = 'a'
print("This is a character: ",letter)
print(type(letter))

name = "Lebron"
print("This is a string: ",name)
print(type(name))

flag1 = False
flag2 = True
print("Those are booleans: ",flag1,flag2)
print(type(flag1))
print(type(flag2))

# list
fruits = ["apple", "mango", "orange"]
print(fruits)
print(type(fruits))

# set
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)
print(type(vowels))

# tuple
numbers = (1, 2, 3)
print(numbers)
print(type(numbers))

# dictionary
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)
print(type(alphabets))


# Python User Input/Output
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)
print('Data type of num:', type(num))

# if-elif-else statement
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')


# Python for Loop
languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for language in languages:
    print(language)


digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


# Python while loop
# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')


# Python break and continue
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# Functions
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

# function call with two values
add_numbers(10, 5)


# Lamda
greet = lambda : print('Hello World')
greet()


# import
"""
As our program grows bigger, it may contain many lines of code.
Instead of putting everything in a single file, we can use modules
to separate codes in separate files as per their functionality.
This makes our code organized and easier to maintain.
We do this using keyword "import"
"""
import math
print(math.sqrt(4))


"""
Now we will explain some NLP concepts:

.pyttsx3: is a text-to-speech conversion library in Python

.Speech Recognition: Library for performing speech recognition,
with support for several engines and APIs, online and offline.

"""