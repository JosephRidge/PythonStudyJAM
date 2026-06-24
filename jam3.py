"""

CONTROL FLOWS: 
    - if..else
    - ternary operator
    - if..elif..else
    - match..case 

LOOPS: 
    - do..while
    - for..in
    
KISS => Keep it Stupid Simple
"""


output = "" # global variable

color = "GREEN"
color_two = "BLUE"

# if..else statement
if color == "GREEN": 
    output = "You can travel!"
    # if color_two == "BLUE":
    #     output ="you have YELLOW"
else:
    output = "wait a minute"

color = "BLUE"
output = "You can proceed" if color =="GREEN" else "wait  minute!" # ternary operator


traffic_light_one = "RED"
traffic_light_two = "GREEN"
traffic_light_three = "ORANGE"

active_light = traffic_light_one
active_light = traffic_light_two

if active_light == "RED": 
    output = "STOP Vehicle"
else: 
    output = "PROCEED TO DESTINATION"

output = "STOP Vechicle!" if active_light == "RED" else "PROCEED TO DESTINATION!"  # ternary operator


if active_light == "RED": 
    output = "STOP Vehicle"
elif active_light == "ORANGE":
    output = "GET READY!"
else: #default when both cases fail
    output = "PROCEED TO DESTINATION"


output
print("==========================================================")
print(output)
print("==========================================================")
 