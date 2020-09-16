#-----------------------------EXAMPLES------------------------------


# Here is an example of using print to display message to the user:

print('Hello, World!')

# Display your own message using print below:

print('HELLO YAAAALLLL')

#-----------------------------EXAMPLE------------------------------

# DO NOT EDIT - Setup for exploration
# tiny number
int1 = 5
float1 = 5.0
# small number
int2 = 135
float2 = 135.246
# huge number known as `googol`
int3 = 10**100
float3 = 10.0**100

# STEP 1: Print and compare tiny numbers
print('** FIVE **')
# 1A: Print int1
print(int1)
# 1B: Print float1
print(float1)
# 1C: Print equality comparison (==) between int1 and float1
print(int1 == float1)

# STEP 2: Print and compare huge numbers
print('\n** GOOGOL **')
# 2A: Print int3
print(int3)
# 2B: Print float3
print(float3)
# 2C: Print equality comparison (==) between int1 and float3
print(int1 == float3)

# STEP 3: Compare results of integer division in all 4 possible combinations
print('\n** INTEGER DIVISION **')
# 3A: Print int2 divided by int1 (//)
print(int2 // int1)
# 3B: Print float2 divided by float1 (//)
print(float2 // float1)
# 3C: Print float2 divided by int1
print(float2 // int1)
# 3D: Print int2 divided by float1
print(int2 // float1)

# STEP 4: Compare results of mod in all 4 possible combinations
print('\n** MOD **')
# Copy/paste 4 statements from STEP 3 and switch operator to mod (from // to %)
print(int2 % int1)
print(float2 % float1)
print(float2 % int1)
print(int2 % float1)



#----------------------------------EXAMPLE--------------------------------------


# DO NOT EDIT - Example of a multiline string
print('''
Here is a whole bunch of instruction that you'd better follow if you know what's good for you!

It even includes blank lines. :)
''')

# STEP 1: Write your own print statement on multiple lines

print(''' 
lexus
is
the

best
''')



# DO NOT EDIT
print('***BEFORE***')

# STEP 2: Copy the original multiline print and make it show
# without blank lines at the beginning and the end
print('Here is a whole bunch of instruction that you\'d better follow if you know what\'s good for you!It even includes blank lines. :)')


# DO NOT EDIT
print('***AFTER***')
print()

# STEP 3: Uncomment the following print command and fix the error
print('What\'s up, doc?')

# STEP 4: Uncomment the following print command and fix the error
print('The poet used "day" to mean "life".')

# STEP 5: Uncomment the following print command and fix the error
print('The bunny said, "Let\'s go to the library."')

# DO NOT EDIT - Sample debug for an equality operation
num = 5
str = "5"
print('num {0}, str {1}, equal? {2}'.format(num, str, num==str))

# STEP 6: Rewrite the print above in an alternate way using f' on the string
print(f'num {num}, str {str}, equal? {num==str}')




#----------------------------------EXAMPLE--------------------------------------

print("** Doubling Penny **")

# How many times would a penny need to double to generate a million dollars?
count = 0
total = 0.01

# STEP 2: Write the while loop

while total < 1000000.00:
  total *= 2
  count += 1


print('Double', count, 'times')

# How much money has been generated at that point?
print('${:,}'.format(total))



#----------------------------------EXAMPLE--------------------------------------
'''
This is a simple script to practice creating a few functions in Python

Please follow the steps outlined below.
'''

# STEP 1 - Write a function named `welcome` that prints a welcome message
def welcome():
  print('welcome!')

# Step 2 - Write a function named `calc_sum` that
#   - takes in two numbers and
#   - returns their sum
def calc_sum(n1, n2):
  return(n1 + n2)


# DO NOT EDIT - The guts of the program
welcome()
print(calc_sum(1,2), 'is 3?', calc_sum(1,2) == 3)
print(calc_sum(-10,-2), 'is -12?', calc_sum(-10,-2) == -12)
print(calc_sum(1.1,-2.2), 'is -1.1?', calc_sum(1.1,-2.2) == -1.1)
print(calc_sum('a','b'), 'is ab?', calc_sum('a','b') == 'ab')
print(calc_sum([1,2],[3,4]), 'is [1,2,3,4]?',
      calc_sum([1,2],[3,4]) == [1,2,3,4])


#----------------------------------EXAMPLE--------------------------------------
# Define your function "addition" here
def addition(n1, n2):
  return n1+n2


print(addition(2, 3))   #> 5
print(addition(-3, -6)) #> -9
print(addition(7, 3))   #> 10



#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def is_same_num(n1, n2):
	return n1 == n2


print(is_same_num(4, 8))   #>  False
print(is_same_num(2, 2))   #>  True
print(is_same_num(2, "2")) #>  False



#----------------------------------EXAMPLE--------------------------------------
# Your function here
# def min2sec(sec):
#   return sec * 60

min2sec = lambda sec: sec * 60

print(min2sec(5)) #> 300
print(min2sec(3)) #> 180
print(min2sec(2)) #> 120



#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
# Parameters are in this order: chickens, cows, pigs
def how_many_legs(chickens, cows, pigs):
  return chickens*2 + (cows+pigs)*4


print(how_many_legs(2, 3, 5))    #> 36
print(how_many_legs(1, 2, 3))    #> 22
print(how_many_legs(5, 2, 8))    #> 50



#----------------------------------EXAMPLE--------------------------------------
# Create your function, here.
increment = lambda n: n+1

print(increment(0))   #> 1
print(increment(9))   #> 10
print(increment(-3))  #> -2



#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def remainder(n1, n2):
  return n1%n2


print(remainder(1, 3))  #> 1
print(remainder(3, 4))  #> 3
print(remainder(5, 5))  #> 0
print(remainder(7, 2))  #> 1



#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def string_int(s):
  return int(s)


print(string_int("6"))     #> 6
print(string_int("1000"))  #> 1000
print(string_int("12"))    #> 12


#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def calculate_exponent(n, e):
  return n**e


print(calculate_exponent(5, 5))     #> 3125
print(calculate_exponent(10, 10))   #> 10000000000
print(calculate_exponent(3, 3))     #> 27



#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def And(a, b):
  return a and b


print(And(True, False))    #> False
print(And(True, True))     #> True
print(And(False, True))    #> False
print(And(False, False))   #> False


#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def long_burp(n):
  return 'Bu' + n*'r' + 'p'


print(long_burp(3))  #> "Burrrp"
print(long_burp(5))  #> "Burrrrrp"
print(long_burp(9))  #> "Burrrrrrrrrp"


#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def cap_space(s):
  res = ''
  i = 0
  while i < len(s):
    char = s[i]
    if char.isupper():
      res += ' '
    
    res += char
    i += 1
  
  return res.lower()


print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"



#----------------------------------EXAMPLE--------------------------------------
# Write your function, here.
def concat_name(a, b):
  # return b + ', ' + a
  return f'{b}, {a}'


print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"


#----------------------------------EXAMPLE--------------------------------------


# Write your function, here.
def char_count(char, s):
  # return s.count(char)
  count = 0
  for c in s:
    if c == char:
    	count += 1
  return count



print(char_count("a", "App Academy"))         #> 1
print(char_count("c", "Chamber of Secrets"))  #> 1
print(char_count("b", "big fat bubble"))      #> 4



#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def factorial(n):
  res = 1
  for i in range(1, n+1):
    res*=i
  
  return res
#   if n == 1:
#     return 1
  
#   return factorial(n-1)*n



print(factorial(1))     #> 1
print(factorial(8))     #> 40320
print(factorial(12))    #> 479001600


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def divisible_by_five(n):
  return n%5==0


print(divisible_by_five(5))    #> True
print(divisible_by_five(-55))  #> True
print(divisible_by_five(37))   #> False


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def is_last_character_n(s):
  return s[-1] == 'n'


print(is_last_character_n("Aiden"))  #> True
print(is_last_character_n("Piet"))   #> False
print(is_last_character_n("Bert"))   #> False
print(is_last_character_n("Dean"))   #> True


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def compare(s1, s2):
  return len(s1) == len(s2)


print(compare("AB", "CD"))              #> True
print(compare("ABC", "DE"))             #> False
print(compare("hello", "App Academy"))  #> False


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def is_valid_hex_code(hex):
  if hex[0] != '#' or len(hex) != 7:
    return False
  
  alpha = 'abcdef'
  i = 1
  while i < len(hex):
    c = hex[i].lower()
    if not c.isdigit():
      if c not in alpha:
        return False
    i += 1
    
  return True
      



print(is_valid_hex_code("#CD5C5C")) #> True
print(is_valid_hex_code("#EAECEE")) #> True
print(is_valid_hex_code("#eaecee")) #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def first_before_second(s, first, second):
    return s.rindex(first) < s.index(second)


print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
# There are hints after the print statements
def seq_of_numbers(s):
  res = ''
  i = 0
  count = 1
  while i < len(s) - 1:
    next = s[i+1]
    curr = s[i]
    if next == curr:
      count += 1
    else:
      res += f'{count}{curr}'
      count = 1
    i += 1
  
  return res + f'{count}{s[-1]}'


print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "111221"

print(seq_of_numbers("111221"))
# This is "three 1s, two 2s, and one 1"
# Prints "312211"

print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13211311123113112211"





###########################################################
# AN ALGORITHM
# An algorithm for performing this without a data structure
# means you have to think about what you're trying to look
# for.
#
# If you scan the string two characters at a time, when they
# change, you know that you have started a new sequence of
# numbers. You can add the current number of characters that
# you've scanned to a result.
#
# For example, say you had "111221". You would start the
# count at 1 and compare the characters at indices 0 and 1.
# Since they are the same, you would increment the current
# count to two, because you will have found two 1s. Then,
# you would compare the characters at indices 1 and 2.
# Again, they are both 1s, so you would increment the count
# to 3. The next comparison, the one at indices 2 and 3
# yields the characters "1" and "2". At this point, the
# characters have changed. The current count is 3, and the
# current character is "1", so you would concatenate those
# onto a result "31". Then, you would set the current count
# back to 1 (because you have found one 2), and continue
# with the same process.


############################################################
# PSEUDOCODE
#
# Concatenate an empty space to the end of the value passed
#    into the function. This will let you compare the entire
#    length of the original string with a guarantee that the
#    two last characters do not match.
# Create an empty string to which you will append the
#    counts and digits
# Initialize an index to 0 for looping over the string
# Initialize a counter variable to record the count of the
#    current character
# Using the index variable, loop from 0 to the length of the
#    string minus 1 (because you don't want to examine the
#    last character, the space that you added)
#   If the current character is not equal to the next
#      character, then concatenate the current count and the
#      current character to the result string and set the
#      current count back to 1
#   Otherwise, just increment the current character count by
#      1
#   Increment the index by 1
# Return the result


