               Equality
# Comparison of booleans
True==False
# Comparison of integers
-5*15!=75
# Comparison of strings
"pyscript"=="PyScript"
# Compare a boolean with an integer
True==1


               Greater and less than
# Comparison of integers
x = -3 * 6
print(x>=-10)
# Comparison of strings
y = "test"
print("test"<=y)
# Comparison of booleans
print(True>False)


                Compare Arrays
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than or equal to 18
print(my_house>=18)
# my_house less than your_house
print(my_house<your_house)                 



                and, or, not (1)
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)
# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)
# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2<your_kitchen*3)


                and, or, not(2)
To see if you completely understood the boolean operators, have a look at the following piece of Python code:
x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10))
What will the result be if you execute these three commands in the IPython Shell?
>> False


                Boolean operators with Numpy
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5,my_house<10))
# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))


                 Warmup
To experiment with if and else a bit, have a look at this code sample:

area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")
What will the output be if you run this piece of code in the IPython Shell?
>> medium


                 If
# Define variables
room = "kit"
area = 14.0
# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")
# if statement for area
if area>15:
    print("big place!")


                 Add else
# Define variables
room = "kit"
area = 14.0
# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")
# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("pretty small.")


                  Customize further : elif
# Define variables
room = "bed"
area = 14.0
# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")
# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area>10:
    print("medium size, nice!")
else :
    print("pretty small.")


                   Driving right(1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Extract drives_right column as Series: dr
dr=cars.loc[:,'drives_right']
# Use dr to subset cars: sel
sel=cars[dr]
# Print sel
print(sel)


                   Driving right(2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Convert code to a one-liner
sel = cars[cars['drives_right']]
# Print sel
print(sel)                   


                    Cars per capita(1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Create car_maniac: observations that have a cars_per_cap over 500
cpc=cars['cars_per_cap']
many_cars=cpc>500
car_maniac=cars[many_cars]
# Print car_maniac
print(car_maniac)


                    Cars per capita(2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Import numpy, you'll need this
import numpy as np
# Create medium: observations with cars_per_cap between 100 and 500
cpc=cars['cars_per_cap']
between=np.logical_and(cpc>100,cpc<500)
medium=cars[between]
# Print medium
print(medium)







































