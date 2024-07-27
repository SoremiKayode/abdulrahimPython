""" 
variable is like a xontainer to stores data value
"""

x = 100 # integer
my_name = "Abdul Faiz" # string
heigh = 4.5 # float

# when you divide it automatically convert to float
# print("x divided by 10", x / 10)
# print(x)
# print(my_name)
# print(heigh)

# casting mean converting from one datatype to another
# casting from interger to string
x_string = str(x)
# print(type(x_string))

# print(type(100.7))

# casting from string to integer
my_score = "666"
# print(type(my_score)) # checking the datatype using type function
my_score_int = int(my_score)

# casting str to float
my_score_float = float(my_score)
print("coverting string to float : ", type(my_score_float))

# converting float to integer
# print(float(100))

poem = """
Tick says the clock,
Tick! Tick!
What you have to do, do quick!
"""

# print(poem)

# overwriting variable
student1 = 34
student1 = 35

print(student1)


""" 
Rules in naming your variable
1. variable can only start with a letter or an underscore
2 a variable can contain a number but cannot start with a number
3. variable name can only contain alphanumeric characters [a-z, A-z, 0-9]
and underscore
4. A variable name are case sensitive age and Age is not the same
5. variable names cannot be python keywords

and	A logical operator
as	To create an alias
assert	For debugging
break	To break out of a loop
class	To define a class
continue	To continue to the next iteration of a loop
def	To define a function
del	To delete an object
elif	Used in conditional statements, same as else if
else	Used in conditional statements
except	Used with exceptions, what to do when an exception occurs
False	Boolean value, result of comparison operations
finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	To create a for loop
from	To import specific parts of a module
global	To declare a global variable
if	To make a conditional statement
import	To import a module
in	To check if a value is present in a list, tuple, etc.
is	To test if two variables are equal
lambda	To create an anonymous function
None	Represents a null value
nonlocal	To declare a non-local variable
not	A logical operator
or	A logical operator
pass	A null statement, a statement that will do nothing
raise	To raise an exception
return	To exit a function and return a value
True	Boolean value, result of comparison operations
try	To make a try...except statement
while	To create a while loop
with	Used to simplify exception handling
yield	To return a list of values from a generator
"""

#1. variable can only start with a letter or an underscore

a = 20
_a = 40
_ = 5
# 4spoon = "treak"

# 2.a variable can contain a number but cannot start with a number
student_1 = 100
all_4 = 45

# variable name can only contain alphanumeric characters [a-z, A-z, 0-9]
# and underscore

aRhjd = 56
_djdj = 100

fff_456 = 5

# variable name are case sensitive
height = 45
Height = 67

# variable cannot contain python keyword
yields = 45

print(yields)
print('=======' * 10)
# Assigning values to a variable
a = 4, 5, 6
print(type(a))
print('=======' * 10)
# we can assign multiple values to multiple variables on a signle line
a, b, c = 3, 4, 5

print("a : ", a)
print("b : ", b)
print("c : ", c)
print('=======' * 10)
# You can assign single value to multiple variables
a = b = c = 40

print("a : ", a, "b : ", b, "c : ", c)
print('=======' * 10)

# Unpacking variable
*student_score1, student_score2, student_score3 = [5, 6, 7, 6, 5, 6, 7, 7]
print("student_score 1 : ",student_score1)
print("student_score 2 : ",student_score2)
print("student_score 3 : ",student_score3)
print('=======' * 10)
# print(5 * 6 + 7 - 3 ** 6)
a  = "==" * 6
print('=======' * 10)

# a variable i a block of code is call local variable
def calMean():
    global a
    a = 5 # local variable

calMean()
print(a)
a = 67 # gobal variable

""" 
pep 8 rules
if you're using variable with multiple name seperate them by underscore
snake case
student_name_one = "Frank"

samething with function
def cal_student_score():
    pass


use camelcase if it is class
class studentName() :
    pass
    
pascal case
def StudentName() :
"""


