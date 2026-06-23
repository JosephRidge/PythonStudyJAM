
"""
DATA TYPES: 
    - Text(strings) :
        - They are enclosed inside a "" or ''
        - is an array of characters (immutable in nature)
        - class <str>: <class 'str'>

    - Numbers(Integers, Floating, Complex):
        - integers:
            - whole numbers that span from -infitnity to +infinity:
            - class <int>: <class 'int'>
        - floatings:
            - decimal numbers
            - class <float>: <class 'float'>
        complex:
            - eg squareroot of 2
            - class <complex>

    - Lists:
        - Array List
            - collection of items(can be repeated)
            - mutable(can be updated)
            - class <list>: <class 'list'>
            - enclosed inside a [] 

        - Tuples:
            - immutable in nature (they cannot be updated)
            - class <tuple>:<class 'tuple'>
            - enclosed in ()
            - items can be repeated
        
        - Set:
            - collection of unique items (items cannot be repeated)
            - enclosed in {}
            - class <set>

        - Dictionaries:
            - collection of key-value pairs
            - class <dict>
            - enclosed in a {}
            - mutable
NOTE: 
    - every data type has its own method(s). References: 

"""

output = "" # global varibale (it can be accessed everywhere within the netire system)
#  Strings: 

first_name = "John Doe" # using double quotes
last_name = 'Wikipedia' # using single quotes

# combining a variable awith a string
ownership = first_name  + " owns a water-melon farm!" # string concatenation
ownership = "That's "+ first_name + "'s "+ "water-melon farm" # string concatenation
ownership = f"That's {first_name}'s water-melon farm!" # using f-string

# accessing elements in a string
name_of_place = "Nairobiey"
output = name_of_place[0] # prints the first characters/ element in a string
output = name_of_place[4] # prints the fifth characters/ element in a string

# slicing - start and stop | start, stop and step  
output = name_of_place[0:3] # start and stop
output = name_of_place[0:3] # start and stop
output = name_of_place[3:] # start and stop

output = name_of_place[0:-1:2] # start, stop, step

# String methods : ref:https://www.w3schools.com/PYTHON/python_ref_string.asp
second_name = "johnowick"
output = second_name.capitalize() # it akes the first letter  to be capital letter
output = second_name.upper() # converting to capital letter
output = second_name.center(2000) #	Returns a centered string  
output = second_name.lower()
output = second_name.count('o') # it returns the count of the occurences of the items 
output = second_name.center(20) #	Returns a centered string  
output = type(second_name) # we invoke th etype command when we want to check the data type 
output = len(second_name) # returns 9
output = len(second_name.center(20)) # returns 20 - due to the added spacing


# Numbers : - integers (whole numbers)
age = 10 
output = type(age) # returns the data type => <class 'int'>
year_of_birth = 2005
current_year = 2026 

output = current_year - year_of_birth

# floating numbers - decimal numbers 
height = 20.5
weight = 40.5 

output = type(height)
height = str(height) # converted ot string
height = float(height) # converting to a floating number
height = int(height) # converting to an integer number
output = type(height)  
output = height

# complex numbers =>  squareroot of 2
sqrt_of_two = 2j # j depicts complex
output = sqrt_of_two
output = type(sqrt_of_two) # <class 'complex'>
age = 10 
output = complex(age)


# Lists(collection of elmements => strings are collections of elments): 
# list 
fruits = ["mango", "banana","apple","pineapple", "watermelon", 100, 20j, 20.54] # arraylist with multiple data types
# fruits.sort() #TypeError: '<' not supported between instances of 'int' and 'str'
fruits = ["mango", "banana","apple","pineapple", "watermelon"] # arraylist  with single data type

# loop for..in loop (running iterations)
# for fruit in fruits:
#     print(fruit) # python groups code using indentation

#  array methods" pop, append, ref: https://www.w3schools.com/python/python_ref_list.asp
fruits.append("kiwi") # method to add an element at the last position in the list
fruits.append("dragon fruit") # method to add an element at the last position in the list
fruits.pop() # delete or drop last element from lists
fruits.insert(1, "orange") # takes two parameters (position and value), places the items at that specific position
fruits.insert(1, "tangerine") # takes two parameters (position and value), places the items at that specific position
fruits.insert(-1, "tangerine") # takes two parameters (position and value), places the items at that specific position
fruits.sort() # arranges in ascending orders

output = fruits
output = type(fruits)
output = fruits[0] # we use indexes to access elements in an array 
output = fruits[-1] # using indexes to access elements
output = fruits[0:4] # slicing
output = fruits [4:] # slicing
ouput = fruits[0:len(fruits)-1:2] # slicing with a step


# Tuples : immutable in nature and enclosed withini  ()
colors = ("RED", "GREEN", "BLUE", "PURPLE", "YELLOW", "WHITE", "RED","BLUE", "RED") 
output = colors
output = colors[0] # accessing it using index
output = colors[0:3] # accessing it using index
output = colors[0:5:2] # slicing with a step

output = type(colors)
output = colors

# tuple mehtods: ref:https://www.w3schools.com/python/python_ref_tuple.asp
output = colors.count("RED") # the number of occurences of the worrd RED
output = colors.index("PURPLE") # return sthe positoin of the elment

# sets: a list composed of unique items , enclosed inside {}
unique_colors = set(colors) # converting a tuple into a set 
output = list(unique_colors) # converting a set into a list 
output = tuple(unique_colors) # converting a list into a tuple 
output = type(unique_colors)

unique_color_codes = {"rouge","brune","noir","blanche","RED"}

#  set methods: ref: https://www.w3schools.com/python/python_ref_set.asp
final_colors = unique_colors.union(unique_color_codes) # joins two sets
final_colors = unique_colors.intersection(unique_color_codes) # what exists in both sets
output = final_colors

# dictionaries: dict=> key: value pairs

person = { 
    "name": "John Doe", 
    "age": 100, 
    "yob": 1926, 
    "isVeteran": False
}
person = { 
    "name": "John Doe", 
    "age": 100, 
    "yob": 1926, 
    "isVeteran": False,
    "hobby": {
        "name": "runnning", 
        "record": "IronMan",
        "year": 2000
    }
}
# dictionary methods: ref:https://www.w3schools.com/python/python_dictionaries_methods.asp
output = person['yob']
output = person.keys()
output = person.values()
output = person["hobby"]
output = person
print("==========================================================")
print(output)
print("==========================================================")
 