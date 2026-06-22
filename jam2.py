
"""
DATA TYPES: 
    - Text(strings) :
        - They are enclosed inside a "" or ''
        - is an array of characters (immutable in nature)
        - class <str>

    - Numbers(Integers, Floating, Complex):
        - integers:
            - whole numbers that span from -infitnity to +infinity:
            - class <int>
        - floatings:
            - decimal numbers
            - class <float>
        complex:
            - eg squareroot of 2
            - class <complex>

    - Lists:
        - Array List
            - collection of items(can be repeated)
            - mutable(can be updated)
            - class <list>
            - enclosed inside a [] 

        - Tuples:
            - immutable in nature (they cannot be updated)
            - class <tuple>
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



print("==========================================================")
print(output)
print("==========================================================")
 