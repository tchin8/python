#----------------------------------EXAMPLE--------------------------------------

# DO NOT EDIT - Starting with a simple lists of colors and numbers
colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
numbers = [2, 34, 8.5, -22.0, 33//4, 2**5]
print ('COLORS', colors)
print ('NUMBERS', numbers)

# 1. Print the total number of colors (length of the list)
print(len(colors))

# 2. Print the first color
print(colors[0])

# 3. Print the second and third colors
print(colors[1:3])

# 4. Print the last two colors
print(colors[-2:])

# 5. Print the smallest number in the numbers list
print(min(numbers))

# 6. Print the largest number in the numbers list
print(max(numbers))

# 7. Sort the numbers
numbers = sorted(numbers)
# Also acceptable: numbers.sort()

# UNCOMMENT WHEN YOU WORK ON #7
print ('SORTED NUMBERS', numbers)

# Sort the colors alphabetically ignoring case
colors = sorted(colors, key=str.lower)
# Also acceptable: colors.sort(key=str.lower)

# UNCOMMENT WHEN YOU WORK ON #8
print ('SORTED COLORS', colors)


#----------------------------------EXAMPLE--------------------------------------

# There are two ways to declare dictionaries
# Create a dictionary and assign it to the d1 variable using the dict()
# constructor that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
d1 = dict(module="Python 3", subject="Dictionaries")


# Create a dictionary and assign it to the d2 variable using the dictionary
# literal that has key/value pairs
#   key: "module", value: "Python 3"
#   key: "subject", value: "Dictionaries"
d2 = {"module": "Python 3", "subject": "Dictionaries"}


# Unlike JavaScript, the keys in Python dictionaries can be any kind of
# value, not just strings or Symbols. Add a key to d1 that is the number
# one with the value "one". Then, add another key to d1 that is a string
# that contains the character 1 and give it the value of "one". Then,
# print the dictionary to see what's in there.
d1[1] = "one"
d1["1"] = "one"
print(d1)


# Convert d1 to a list using the list() method. Then, print it. What gets
# put into the list?
d1_as_list = list(d1)
print(d1_as_list)


# Now, check that the following keys are in d1 by printing out if
# they do exist. The first one is there for you.
#  "module"    should be True
#  "subject"   should be True
#  "age"       should be False
#  1           should be True
#  "1"         should be True
#  "one"       should be False
#  True        should be False
print(f"'module' in d1? {'module' in d1}")



#----------------------------------EXAMPLE--------------------------------------

# DO NOT EDIT
odds = 1,3,5,7,9
evens = 2,4,6,8

# Step 1: Print out the result of adding evens to odds
print(odds+evens)

# Step 2: Print out the result of multiplying odds by three
print(odds*3)

# Step 3A: Use print to find out if odds is less than evens
print(odds < evens)

# Step 3B: Print out your explanation of why 3A has that result
print('First item in odds (1) is < first item in evens (2), so odds < evens.')

# Step 4: Print out the average of the numbers in evens using one line of code
print(sum(evens)/len(evens))

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)
def minmaxmean(iterable):
    return min(iterable), max(iterable), sum(iterable)/len(iterable)

# Step 5B: Use print to confirm you function is working on evens and odds
print(minmaxmean(evens))
print(minmaxmean(odds))

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way
(low,high,ave) = minmaxmean((22, 33, 44, 55, -7, 16, 123))
print('Average is {2} with range from {0} to {1}.'.format(low, high, ave))


#----------------------------------EXAMPLE--------------------------------------

print('THREE CASES FOR RANGE')
print('A) End Value')

# STEP 1: Change the zero in the range to 10
#         Notice how "10" is not included in the output
for i in range(10):
    print(i)

print('B) Start & End Values')

# STEP 2: Code a `for` loop to print numbers 5 through 9
for i in range(5, 10):
	print(i)

print('C) Only Even Values')

# STEP 3: Print 0, 2, 4, 6 and 8 using a for loop
#         Hint - range can take a 3rd parameter for the step distance
for i in range(0, 9, 2):
	print(i)


#----------------------------------EXAMPLE--------------------------------------

# Powers of 2 from 1 to 16
# Write a for loop that uses the range function to
# print the powers of 2 from 2 - 65536, that is
# from 2^1st - 2^16th powers

for i in range(1,17):
  print(2**i)


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def get_first_value(list):
  return list[0]


print(get_first_value([1, 2, 3]))        #> 1
print(get_first_value([80, 5, 100]))     #> 80
print(get_first_value([-500, 0, 50]))    #> -500


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
get_sum_of_elements = lambda l: sum(l)


print(get_sum_of_elements([2, 7, 4]))     #> 13
print(get_sum_of_elements([45, 3, 0]))    #> 48
print(get_sum_of_elements([-2, 84, 23]))  #> 105


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def get_indices(l, char):
  idx = []
  for i in range(0, len(l)):
    if l[i] == char:
      idx.append(i)
  return idx



print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
# Prints [0, 1, 3, 5]

print(get_indices([1, 5, 5, 2, 7], 7))
# Prints [4]

print(get_indices([1, 5, 5, 2, 7], 5))
# Prints [1, 2]

print(get_indices([1, 5, 5, 2, 7], 8))
# Prints []


#----------------------------------EXAMPLE--------------------------------------

# Your code, here.
can_nest = lambda l1, l2: min(l1) > min(l2) and max(l1) < max(l2)


print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
print(can_nest([3, 1], [4, 0]))        #> True
print(can_nest([9, 9, 8], [8, 9]))     #> False
print(can_nest([1, 2, 3, 4], [2, 3]))  #> False


#----------------------------------EXAMPLE--------------------------------------

GUEST_LIST = {
  "Kurt": "Germany",
  "Julia": "France",
  "Ito": "Japan",
  "Katherine": "England",
  "Sam": "Argentina"
}

# Write your function, here.
def greeting(name):
  if name not in GUEST_LIST:
    return "Hi! I'm a guest."
  else:
    return f'Hi! I\'m {name} from {GUEST_LIST[name]}.'


print(greeting("Kurt"))   #> "Hi! I'm Kurt from Germany."
print(greeting("Sam"))    #> "Hi! I'm Sam from Argentina."
print(greeting("Monty"))  #> "Hi! I'm a guest."


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
has_key = lambda dict, ele: ele in dict 


print(has_key({ "a": 44, "b": 45, "c": 46 }, "d"))
# False

print(has_key({ "craves": True, "midnight": True, "snack": True }, "morning"))
# False

print(has_key({ "pot": 1, "tot": 2, "not": 3 }, "not"))
# True


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
find_smallest_num = lambda l: min(l)


print(find_smallest_num([34, 15, 88, 2]))                   #> 2
print(find_smallest_num([34, -345, -1, 100]))               #> -345
print(find_smallest_num([-76, 1.345, 1, 0]))                #> -76
print(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999])) #> -0.9999
print(find_smallest_num([7, 7, 7]))                         #> 7


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
is_empty = lambda d: not d


print(is_empty({}))        #> True
print(is_empty({"a": 1}))  #> False


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def difference(l):
  return max(l) - min(l)


print(difference([10, 15, 20, 2, 10, 6]))
# 20 - 2 = 18

print(difference([-3, 4, -9, -1, -2, 15]))
# 15 - (-9) = 24

print(difference([4, 17, 12, 2, 10, 2]))
# 17 - 2 = 15


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
first_last = lambda l: [l[0], l[-1]]


print(first_last([5, 10, 15, 20, 25]))            #> [5, 25]
print(first_last([13, None, False, True]))        #> [13, True]
print(first_last([None, 4, "6", "hello", None]))  #> [None, None]


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def find_digit_amount(num):
  if num < 0:
    return len(str(num))-1
  return len(str(num))



print(find_digit_amount(123))           #> 3
print(find_digit_amount(-56))           #> 2
print(find_digit_amount(7154))          #> 4
print(find_digit_amount(61217311514))   #> 11
print(find_digit_amount(0))             #> 1


#----------------------------------EXAMPLE--------------------------------------

# Write your function, here.
def track_robot(dirs):
  coord = [0, 0]
  if not len(dirs):
    return coord
  
  for i in range(0, len(dirs)):
    dir, num = dirs[i].split()
    if dir == 'right':
        coord[0] += int(num)
    elif dir == 'left':
      	coord[0] -= int(num)
    elif dir == 'up':
      coord[1] += int(num)
    else:
      coord[1] -= int(num)
  return coord

# # Write your function, here.
# def track_robot(instructions):
#     totals = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
#     for step in instructions:
#         step = step.split()
#         totals[step[0]] += int(step[1])
#     return [totals['right'] - totals['left'], totals['up'] - totals['down']]


print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]


#----------------------------------EXAMPLE--------------------------------------

# STEP 1: Complete analyze function to return 5 values:
#    - minimum
#    - maximum
#    - mean (a.k.a. average)
#    - median (center point)
#    - mode (most repeated)
def analyze(nums):
    return (
        min(nums),
        max(nums),
        sum(nums)/len(nums),
        median(nums),
        mode(nums)
    )

# STEP 2: Complete median function to return center number
#         WITHOUT using built-in function
def median(nums):
    # if there are no numbers, then exit right away
    if (len(nums) == 0):
        return 0

    # sort numbers and find the middle
    orderedNums = sorted(nums)
    midIndex = len(orderedNums) // 2

    # if there's an odd number, use the number in the middle
    if (len(orderedNums) % 2 == 1):
        return(orderedNums[midIndex])

    # if there's an even number, use average of two elements in the middle
    return((orderedNums[midIndex] + orderedNums[midIndex-1]) / 2)

# STEP 3: Complete mode function to return most-repeated number
#         WITHOUT using built-in function
def mode(nums):
    # build a dictionary to track the element counts
    lookup = dict.fromkeys(nums, 0)
    for x in nums:
        lookup[x] += 1

    # make parallel arrays of the numbers (elements) and counts
    counts = list(lookup.values())
    elements = list(lookup.keys())

    # find the largest count and its position
    highCount = max(counts)
    highAt = counts.index(highCount)

    # BONUS B: Catch special case where more than one value repeats the most
    counts.sort()
    if (len(nums) > 1 and (len(counts) == 1 or counts[-2] == highCount)):
        return

    # mode is the number corresponding to the highest count
    return(elements[highAt])

# DO NOT EDIT - sample data for checking your work
sample1 = 1,2,3,4,5,6,7,8,9
sample2 = [37,45,23,65,75,34,23,23,23,65,12,99]

print(('min', 'max', 'mean', 'median', 'mode'))
print(analyze(sample1))
print(analyze(sample2))

# BONUS A: Print more samples as you see fit
print(analyze([0]))
print(analyze([1,1,1,1,1]))


#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------




#----------------------------------EXAMPLE--------------------------------------







