# =============================================================================
# Title             PyHacks - In-Built Python Function
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      06/04/2021
# =============================================================================


def padd_with_stuff(text):
    print('-'*80)
    print(text)
    print('-'*80)

# All
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
#If the iterable object is empty, the all() function also returns True.

padd_with_stuff('All() function')
mylist = [True, True, True]
x = all(mylist)
print(x)


# Any function
# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.
padd_with_stuff('Any() function')
mylist = [False, True, False]
x = any(mylist)
print(x)

# Ascii text
padd_with_stuff('ascii() function')
x = ascii('My name is Gary')
print(x)

# bin - binary version of a number
padd_with_stuff('bin() function')
x = bin(36)
print(x)

# Bool() - returns the boolean
padd_with_stuff('bool() function')
x = bool(1)
print(x)

# bytearray() converts objects into bytearrays
padd_with_stuff('bytearray function')
x = bytearray(4)
print(x)

# Returns a bytes function
padd_with_stuff('bytes function')
x = bytes(4)
print(x)


# Callable - check if a function is callable
padd_with_stuff('callable() function - check if func is callable')
def x():
    a = 5

print(callable(x))

# chr() function - get the character that represents the unicode 97
padd_with_stuff('chr() function')
x = chr(97)
print(x)

# Compile - compile text as code and then execute it
padd_with_stuff('compile() function')
x = compile('print(55)', 'test', 'eval')
exec(x)

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)

# Complex - return a complex number
padd_with_stuff('complex() function')
x = complex('3+5j')
print(x)

# delattr() - deletes a specific attribute from a specific object
padd_with_stuff('delattr() function')
class Person:
    name = 'Gary'
    age = 39
    country = 'England'

delattr(Person, 'age')
print(Person.name)

# Dict() return a dictionary array
padd_with_stuff('Dict() function')
x = dict(name = "John", age = 36, country = "Norway")
print(x)

# dir() function - returns all properties and methods of the specified object
padd_with_stuff('dir() function - return all properties and methods from class or object')
class Person:
    name = 'Gary'
    age = 39
    country = 'England'

print(dir(Person))

# divmod() function - display the quotient and the remainder of 5 divided by 2
padd_with_stuff('divmod() function - get the modulo')
x = divmod(5,2)
print(x)

# Enumerate - adds a counter to the key of an enumerate object
padd_with_stuff('enumerate() function - add counter')
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(x,y)

# Evaluates and executes and expession - eval()
padd_with_stuff('eval() function')
x = "print(55)"
eval(x)

# Exec() execute specific code or object
padd_with_stuff('exec() function')
x = 'name = "Gary"\nprint(name)'
exec(x)

# Filter() - filter the array and return a new array with only the values
padd_with_stuff('filter() function')
ages = [5,12,17,18,24,32]
def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults: 
    print(f'Age is: {x}')


# Float function
padd_with_stuff('Float function')
x = float(3)
print(x)

# Format function - format a specific value
padd_with_stuff('format() function')
# '<' - Left aligns the result (within the available space)
# '>' - Right aligns the result (within the available space)
# '^' - Center aligns the result (within the available space)
# '=' - Places the sign to the left most position
# '+' - Use a plus sign to indicate if the result is positive or negative
# '-' - Use a minus sign for negative values only
# ' ' - Use a leading space for positive numbers
# ',' - Use a comma as a thousand separator
# '_' - Use a underscore as a thousand separator
# 'b' - Binary format
# 'c' - Converts the value into the corresponding unicode character
# 'd' - Decimal format
# 'e' - Scientific format, with a lower case e
# 'E' - Scientific format, with an upper case E
# 'f' - Fix point number format
# 'F' - Fix point number format, upper case
# 'g' - General format
# 'G' - General format (using a upper case E for scientific notations)
# 'o' - Octal format
# 'x' - Hex format, lower case
# 'X' - Hex format, upper case
# 'n' - Number format
# '%' - Percentage format

x = format(0.5, '%')
print(x)

# Frozenset fronzenset() function
padd_with_stuff('frozenset() function')
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
# This is unchangable


# getattr() function
padd_with_stuff('getattr() function - gets attributes of specified objects')
class Person:
    name = 'Gary'
    age = 39
    country='England'

x = getattr(Person, 'age')
print(x)
y = getattr(Person, 'page', 'my message')
print(y)

# Globals - returns the current globals symbols as a dictionary
padd_with_stuff('globals()')
x = globals()
print(x)

# hasattr() function
padd_with_stuff('hasattr() function - returns boolean if attribute exists')
class Person: 
    name = 'Another person'
    age = 99
    country = 'Norway'

x = hasattr(Person, 'age')
print(x)

# hex - converts a number into a hexidecimal value
padd_with_stuff('hex() function - convert number to hex')
x = hex(255)
print(x)

#id function
padd_with_stuff('id() returns the id of a tuple object')
x = ('foo fighters', 'nirvana', 'soundgarden')
y = id(x)
print(y)

# input() allow user input
# padd_with_stuff('input() function - get user input')
# print('Enter user name:')
# x = input()
# print('Hello, ' + x)

# int() function to convert float into int
padd_with_stuff('int() function - casting to integer')
x = int(3.5)
print(x)

#isinstance() function
padd_with_stuff('isinstance() function')
x = isinstance(5, int)
print(x)

check = isinstance('Hello', (float, int, str, list, dict, tuple))
print(check)

# Class instances
class myObj:
    name = 'Gary'

y = myObj()
x = isinstance(y, myObj)
print(x)


# issubclass() 
padd_with_stuff('issubclass() function')
class myAge:
    age = 39

class myObj(myAge):
    name = 'Gary'
    age = myAge

x = issubclass(myObj, myAge)
print(x)

# iter() function
padd_with_stuff('iter() function')
x = iter(['apple', 'banana', 'cherry'])
print(next(x))
print(next(x))
print(next(x))


# len() function 
padd_with_stuff('Get the length with len()')
mylist = ['apple', 'banana', 'cherry']
x = len(mylist)
print(x)

# Length of string
mylist = 'Hello'
x = len(mylist)
print(x)

# list() to return a list
padd_with_stuff('list() to return a list')
x = list(('apple', 'banana', 'cherry'))
print(x)

# Locals() return a symbol tables as a dictionary
padd_with_stuff('locals() return the local symbol table')
x = locals()
print(x)


# Map() a function to an iterable
padd_with_stuff('map() function to iterable')
def myfunc(n):
    return len(n)

x = map(myFunc, ('apple', 'banana', 'cherry'))
print(x)

# max() largest item in iterable
padd_with_stuff('max() function')
x = max(5,10)
print(x)

# memoryview() function
padd_with_stuff('memoryview() function')
x = memoryview(b'Hello')
print(x)
print(x[0]) #Get the unicode of H in zeroth index

# min() function
padd_with_stuff('min() function over iterable')
x = min(5,10)
print(x)

# object() function - create an empty object
padd_with_stuff('Create object()')
x = object()
print(x)

# Oct() function
padd_with_stuff('oct() function')
x = oct(12)
print(x)

# ord() function
padd_with_stuff('ord() function')
x = ord('h')
print(x)

# pow() function
padd_with_stuff('Get the pow() of a number')
x = pow(4,3)
print(x)

# range() function 
padd_with_stuff('range() function')
x = range(6)
for n in x:
    print(n +1)


# reversed() function
padd_with_stuff('reversed() function')
alph = ['a','b','c','d','e']
ralph = reversed(alph)
for x in ralph:
    print(x)


# round() function
padd_with_stuff('round() function')
x = round(5.76543,2)
print(x)

# set() function
padd_with_stuff('set() function')
x = set(('apple', 'banana', 'cherry'))
print(x)

#setattr() function
padd_with_stuff('setattr() class function to set attributes')
class Person:
    name = 'Gary'
    age = 39
    country = 'England'
setattr(Person, 'age', 40)
print(Person.age)

#slice() function
padd_with_stuff('Slicing the first 2 items from tuples')
a = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
x = slice(2)
print(a[x])

# sorted() function 
padd_with_stuff('sorted() function')
a = ('b','g', 'a', 'd', 'f', 'c', 'h', 'e')
x = sorted(a)
print(x)

#str function
padd_with_stuff('str() function')
x = str(3.5)
print(x)

# sum function
padd_with_stuff('sum() function')
a = (1,2,3,4)
x = sum(a)
b = [1,2,3,4]
y = sum(b)
c = {1,2,3,4}
z = sum(c)
print(x,y, z)

# super function
padd_with_stuff('super() function')
class Parent:
    def __init__(self, txt):
        self.message = txt

    def print_message(self):
        print(self.message)

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

x = Child('Hello, and welcome')
x.print_message()

# tuple() returns a tuple
padd_with_stuff('tuple() function')
x = tuple(('apple', 'banana', 'cherry'))
print(x)

# type() returns a type
padd_with_stuff('type() function')
a = ('apple', 'banana', 'cherry')
b = 'Hello World!'
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x,y,z)

# vars function 
padd_with_stuff('vars() function')
class Person:
    name = 'Gary'
    age = 39
    country = 'England'

x = vars(Person)
print(x)
print(x['name'])

#zip function 
padd_with_stuff('zip() function')
a = ('John', 'Gary', 'Charlie')
b = ('Kerry', 'Pat', 'Joel')
x = zip(a,b)
print(x)
