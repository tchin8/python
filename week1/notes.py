#------------------------------------Numbers-----------------------------------

# integers
print(3)         # => 3
print(int(19))   # => 19
print(int())     # => 0


# floating point number
a = 4.1 - 3
print(a)  # 1.0999999999999996 ???


print(2.24)      # => 2.24
print(2.)        # => 2.0
print(float())   # => 0.0
print(27e-5)     # => 0.00027


# complex numbers
print(7j)             # => 7j
print(5.1+7.7j)       # => 5.1+7.7j
print(complex(3, 5))  # => 3+5j
print(complex(17))    # => 17+0j
print(complex())      # => 0j


# ------------------------------------------------------------------------------
# Type casting
# Example 1: Type-cast float to integer using float
print(17)               # => 17
print(float(17))        # => 17.0

# Example 2: Type-cast float to integer using int
print(17.0)             # => 17.0
print(int(17.0))        # => 17

# Example 3: Type-cast float or integer to string using str
print(str(17.0) + ' and ' + str(17))        # => 17.0 and 17


"""
For example

print(17.0 + ' and ' + 17)
results in

TypeError: unsupported operand type(s) for +: 'float' and 'str'
"""


# Exponentiation
print(2**3)        # => 8
print(5.5**15)     # => 127479497357.65536
print(10**30)      # => 1000000000000000000000000000000
print(10.0**30)    # => 1e+30



#------------------------------------String-----------------------------------

"This is cool!"
'a1b2c3'
'Jodi asked, "What\'s up, Sam?"'

# # Invalid string
# "Tom shouted, "Go outside!""


print('''My instructions are very long so to make them
more readable in the code I am putting them on
more than one line. I can even include "quotes"
of any kind because they won't get confused with
the end of the string!''')


# Calculating length
print(len("Spaghetti"))    # => 9


# Indexing a string
print("Spaghetti"[0])    # => S
print("Spaghetti"[4])    # => h

print("Spaghetti"[-1])    # => i
print("Spaghetti"[-4])    # => e


# like ruby's str[1...4] 
print("Spaghetti"[1:4])  # => pag
print("Spaghetti"[4:-1])    # => hett
print("Spaghetti"[4:4])  # => (empty string)

# A shortcut for the beginning of the string is to omit the first number.
print("Spaghetti"[:4])  # => Spag
print("Spaghetti"[:-1])    # => Spaghett


# A shortcut for the end of the string is to omit the second number.
print("Spaghetti"[1:])  # => paghetti
print("Spaghetti"[-4:])    # => etti


# errors
print("Spaghetti"[15])    # => IndexError: string index out of range
print("Spaghetti"[-15])    # => IndexError: string index out of range

# ranges do not error
print("Spaghetti"[:15])    # => Spaghetti
print("Spaghetti"[15:])    # => (empty string)
print("Spaghetti"[-15:])    # => Spaghetti
print("Spaghetti"[:-15])    # => (empty string)
print("Spaghetti"[15:20])    # => (empty string)



print("Spaghetti".index("h"))    # => 4
print("Spaghetti".index("t"))    # => 6
print("Spaghetti".index("s"))    # => ValueError: substring not found

print("Spaghetti".count("h"))    # => 1
print("Spaghetti".count("t"))    # => 2
print("Spaghetti".count("s"))    # => 0
print('''We choose to go to the moon in this decade and do the other things,
not because they are easy, but because they are hard, because that goal will
serve to organize and measure the best of our energies and skills, because that
challenge is one that we are willing to accept, one we are unwilling to
postpone, and one which we intend to win, and the others, too.
'''.count('the '))                # => 4

print("gold" + "fish")    # => goldfish
print("s"*5)              # => sssss
print("$1" + ",000"*3)     # => 1,000,000,000



### formatting
first_name = "Billy"
last_name = "Bob"
print('Your name is {0} {1}'.format(first_name, last_name))  # => Your name is Billy Bob

print(f'Your name is {first_name} {last_name}')



### String methods
s = "--".join(["it", "is", "kind"])
print(s)

# Prints it--is--kind


#------------------------------------Variables-----------------------------------
### Assigning Variables
a = 7
b = 'Marbles'
print(a)         # => 7
print(b)         # => Marbles


count = max = min = 0
print(count)           # => 0
print(max)             # => 0
print(min)             # => 0


### Manipulating Variables
a = 17
print(a)         # => 17
a = 'seventeen'
print(a)         # => seventeen

'''The assignment shorthand operators from JavaScript also work in Python:

+=
-=
*=
/=
In fact, all the arithmetic operators have shorthand counterparts:

**= (exponent)
//= (integer division)
%= (modulo)'''




### None
my_var = None
print(my_var is None)     # => True




#------------------------------------Boolean-----------------------------------
# Logical AND
print(True and True)    # => True
print(True and False)   # => False
print(False and False)  # => False

# Logical OR
print(True or True)     # => True
print(True or False)    # => True
print(False or False)   # => False

# Logical NOT
print(not True)             # => False
print(not False and True)   # => True
print(not True or False)    # => False



#-----------------------------Comparison Operators------------------------------

a = 4 
b = 5
print(not a == b)     # => True

print(a == not b)    # => SyntaxError

print (a == (not b))    # => False


#-----------------------------Identity Vs. Equality------------------------------

print (2 == '2')    # => False
print (2 is '2')    # => False

print ("2" == '2')    # => True
print ("2" is '2')    # => True

print (2 == 2.0)    # => True
print (2 is 2.0)    # => False



#-----------------------------If Statement------------------------------

if (name == 'Monica'):
  print('Hi, Monica.')


if name == 'Monica':
  print('Hi, Monica.')
else:
  print('Hello, stranger.')


if name == 'Monica':
  print('Hi, Monica.')
elif age < 12:
  print('You are not Monica, kiddo.')



if name == 'Monica':
  print('Hi, Monica.')
elif age < 12:
  print('You are not Monica, kiddo.')
elif age > 2000:
  print('Unlike you, Monica is not an undead, immortal vampire.')
elif age > 100:
  print('You are not Monica, grannie.')


if name == 'Monica':
  print('Hi, Monica.')
elif age < 12:
  print('You are not Monica, kiddo.')
else:
  print('You are neither Monica nor a little kid.')


#-----------------------------While Statements------------------------------

spam = 0
while spam < 5:
  print('Hello, world.')
  spam = spam + 1


# breaking out early 

spam = 0
while True:
  print('Hello, world.')
  spam = spam + 1
  if spam >= 5:
    break



#continue 
spam = 0
while True:
  print('Hello, world.')
  spam = spam + 1
  if spam < 5:
    continue
  break

#-----------------------------Try, Except Statements----------------------------

a = 321
print(len(a))     #TypeError: object of type 'int' has no len()


a = 321
try:
    print(len(a))
except:
    print('Silently handle error here')

    # Optionally include a correction to the issue
    a = str(a)
    print(len(a))


##########

a = 100
b = 0
c = a / b
print(c)      # ZeroDivisionError: division by zero


a = 100
b = 0
try:
    c = a / b
except ZeroDivisionError:
    c = None
print(c)      # None



a = 100
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    pass




a = 100
# b = "5"
try:
    print(a / b)
except ZeroDivisionError:
    pass
except (TypeError, NameError):
    print("ERROR!")



# You can name the error so you can record it!

a = 100
# b = "5"
try:
    print(a / b)
except ZeroDivisionError:
    pass
except (TypeError, NameError) as e:
    print("ERROR!", e)          # ERROR! name 'b' is not defined




# tuple of file names
files = ('one.txt', 'two.txt', 'three.txt')

# simple loop
for filename in files:
    try:
        # open the file in read mode
        f = open(filename, 'r')
    except OSError:
        # handle the case where file does not exist or permission is denied
        print('cannot open file', filename)
    else:
        # do stuff with the file object (f)
        print(filename, 'opened successfully')
        print('found', len(f.readlines()), 'lines')
        f.close()



### without else 

# tuple of file names
files = ('one.txt', 'two.txt', 'three.txt')

# simple loop
for filename in files:
    # CHANGE 1 or 2: Set f to none so we can check it later
    f = None
    try:
        # open the file in read mode
        f = open(filename, 'r')
    except OSError:
        # handle the case where file does not exist or permission is denied
        print('cannot open file', filename)
    
    # CHANGE 2 of 2: Check the value of f (None is equivalent to false)
    if f:
        # do stuff with the file object (f)
        print(filename, 'opened successfully')
        print('found', len(f.readlines()), 'lines')
        f.close()



### finally
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result is", result)
    finally:
        print("Finally...")


# FINALLY RUNS BEFORE ANY RETURNS IN TRY OR EXCEPTION
def greeting():
    try:
        return "Hey, friend."
    finally:
        return "Fun times!"

print(greeting())



### hasattr

# Try a number - nothing will print out
a = 321
if hasattr(a, '__len__'):
    print(len(a))

# Try a string - the length will print out (4 in this case)
b = "5555"
if hasattr(b, '__len__'):
    print(len(b))



### pass ###
# use pass if a clause is empty
if True:
  pass


while True:
  pass

# THIS CODE WILL RESULT IN AN IndentationError
print("Hello")

if True:

print("Good-bye")


#----------------------------------Functions-----------------------------------

def printCopyright():
    print("Copyright 2020. Me, myself and I. All rights reserved.")


def average(num1, num2):
    return (num1/num2)

print(average(6, 2))        # => 3.0


def greeting(name, saying="Hello"):
    print(saying, name)

greeting("Monica")
# Hello Monica

greeting("Barry", "Hey")
# Hey Barry




# THIS IS BAD CODE AND WILL NOT RUN
def increment(delta=1, value):
    return delta + value



def greeting(name, saying="Hello"):
    print(saying, name)

greeting("Monica")
# Hello Monica

greeting("Monica", saying="Hi")

greeting(name="Barry", saying="Hey")
# Hey Barry

greeting(saying="Hey", name="Barry")
# Hey Barry



#----------------------------------Classes-----------------------------------
#----------------------------------Classes-----------------------------------

class AngryBird:
  def __init__(self):
    """
    Construct a new AngryBird by setting its position to (0, 0).
    """
    self.x = 0
    self.y = 0

  def move_up_by(self, delta):
    self.y += delta


bird = AngryBird()
print(bird.x, bird.y)  #> 0 0

bird.move_up_by(8)
print(bird.x, bird.y)  #> 0 8

chuck = AngryBird()
matilda = AngryBird()

chuck.move_up_by(13)
matilda.move_up_by(-4)

print(chuck.x, chuck.y)      #> 0 13
print(matilda.x, matilda.y)  #> 0 -4




# or

class AngryBird:
  def __init__(self, x=0, y=0):
    """
    Construct a new AngryBird by setting its position to (0, 0).
    """
    self.x = x
    self.y = y

  def move_up_by(self, delta):
    self.y += delta

b1 = AngryBird()
b2 = AngryBird(x=1)
b3 = AngryBird(y=18)
b4 = AngryBird(10, 10)




class AngryBird:
    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y




class AngryBird:
    __slots__ = ['_x', '_y']

    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class AngryBird:
    __slots__ = ['_x', '_y']

    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __repr__(self):
        return f"<AngryBird ({self._x}, {self._y})>"




#----------------------------------Inheritance----------------------------------


class Employee:
    def __init__(self, id):
        self.id = id


class Manager(Employee):
    def __init__(self, id):
        super().__init__(id)
        self.employees = []

    def add_direct_report(self, employee):
        self.employees.append(employee)








class Parent:
    def boop(self):
        print("I am Parent#boop")


class Child(Parent):
    def boop(self):
        print("I am Child#boop")
        super().boop()


Child().boop()
# Prints
# "I am Child#boop"
# "I am Parent#boop"




#----------------------------------Properties----------------------------------
class AngryBird:
    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


bird = AngryBird()

print(bird.x, bird.y)



# setters 
class AngryBird:
    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            value = 0
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            value = 0
        self._y = value

bird = AngryBird()
bird.x = 12
bird.y = -20 # Won't get set because of the setter method

print(bird.x, bird.y)  #> 12 0



#------------------------------List Comprehensions------------------------------

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)
# Prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# Using map()

squares = map(lambda x: x**2, range(10))

print(list(squares))
# Prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# Using list comprehensions

squares = [i**2 for i in range(10)]

print(list(squares))
# Prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Using conditional logic

sentence = 'the rocket came back from mars'
vowels = [c for c in sentence if c in 'aeiou']

print(vowels)
# Prints ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']




# ex 2

sentence = 'Mary, Mary, quite contrary, how does your garden grow?'
def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]

print(consonants)
# Prints ['M', 'r', 'y', 'M', 'r', 'y', 'q', 't', 'c',
# 'n', 't', 'r', 'r', 'y', 'h', 'w', 'd', 's', 'y',
# 'r', 'g', 'r', 'd', 'n', 'g', 'r', 'w']




# ex 3

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]

print(prices)
# Prints [1.25, 0, 10.22, 3.78, 0, 1.16]



#   ex 4

def get_price(price):
    return price if price > 0 else 0
prices = [get_price(i) for i in original_prices]

print(prices)
# Prints [1.25, 0, 10.22, 3.78, 0, 1.16]



# matrices

matrix = [[i for i in range(5)] for _ in range(6)]

print(matrix)
# Prints
# [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4]
# ]


# flatten a matrix

matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = [num for row in matrix for num in row]

print(flat)
# Prints [0, 0, 0, 1, 1, 1, 2, 2, 2]