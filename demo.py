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
