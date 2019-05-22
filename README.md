# python-linuxacademy
Python Course


# Lessons

convert python file to executable
cp test.py test
chmod u+x test
$./test

comments

'#one line'
"""multiline
test
"""
len(x) = lenght

# data types

##strings
"test"

'"test"+"ing"'
'testing'

'''multiline
string
'''

'"HA"*4'
'HAHAHAHA'

string methods
'"single".find('g)
'3'

print("show variable : %s" % var)
## Numbers

x // y  int division
x% y  mod
x**3   or  pow(x,3)  exponent
str('7.00')  convert to string


## booleans and none

NONE null


bool(0) = false
bool(1) = true


##vars

myname = "jrab66"
print(myname)

## Lists
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

my_list= [1,2,3,4,5]
my_list[i]

my_list[2:4] = range
my_list[::2] = exclude 2 index
my_list[::-1] = reverse list

my_list.pop = remove last element // stack 
my_list.pop(0) = remove first element // queue
my_list.append(5) = add the element to the list
my_list.insert(index,item) = add element to certain place


## tuples

inmutable fixed size or modified

tuple= (2,3,4)

## Range //less resources (less ram footprint)
range(10) == list(range(10))== [0,1,2,3,4,5,6,7,8,9]
range(1,12,2) == range(start,end,step) 
list(range(1,12,2))==[1,3,5,7,9,11]

## Dictionaries
hashes 
keys are inmutables 

ages={'dog': 29, 'cat':12,'fish': 1}
ages['dog'] == 29

#adding item
ages['turtles']=40
#remove
del ages['dog']
ages.pop('dog')
#values
ages.values()
 weights = dict(kevin=160, bob=240, kayla=135)
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
>>> colors
{'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}



#Statements
https://docs.python.org/3/tutorial/controlflow.html#if-statements

##comparisons
Operation	Meaning
<	strictly less than
<=	less than or equal
>	strictly greater than
>=	greater than or equal
==	equal
!=	not equal
is	object identity
is not	negated object identity

##in
2 in [1,2,3] == true
4 in [1,2,3] == false
4 not in [1,2,3] == true


##Logic operations
#not
not True == False
#or
'' or 'test' == test
#and
1>2 and 1>3 == false

#if
if 1<2: 
    print("dope")

#continue
if count %2 ==0:
    count += 1
    continue

#While
while count <=4:
    print("looping")
    count += 1

#for
colors=['blue','green','red','black']
for color in colors:
    print(color)

for letter in "my_string":
    print(letter)
# for //return dict
for name,age in ages.items():
    print("name: %s" %name)
    print("age: %s" %age)
  
#functions

def hello_world():
    print("Hello World"

def contact_card(name,age,car_model):
    return card+age+car_model

>>> contact_card('jose','20','tesla')
#otherway
>>> contact_card('age=28','car_model=tesla','name=Jose')
#default def // only change when invoking from call
def can_drive(age, driving_age=16):
    return age>=driving_age
////
```
can_drive(22)
can_drive(22,18)
```

Classes

class use camel case 

use pass to omit some def 
```
def test(self):
    logic
    pass
```

importing classes

all class
"""
import math
"""

only part
```
from math import pi
from tireclass import Tire
```



using doctest
```
 python3 -m doctest -v tireclass.py 
```