from os import environ
# escape sequence '\'
print("The doctor's advice, \"I am very happy\".")
print('The doctor\'s advice, "I am very happy".')

# print in paragraph form '''
print('''Under the hood of a car, you'll find a variety of essential components including the engine, battery, radiator, air filter, 
      and various fluid reservoirs like those for engine oil, coolant, brake fluid, and windshield washer fluid. Other notable parts 
      include the alternator, serpentine belt, and fuse box. ''')

# print statement gives output on new line. It is default behavior
# end keyword is used to customize new line
# \n, \t is escape sequence
print("M",end='\t')
print("Umar")
print("Islam",end='\n')
# default seperator is space but we can customize it
print('muhammad','umar', 'islam', sep='---')

''' comments are additional information for later when we forget what code does what
comments are used in debugging as well'''

""" Docstring: Anything written inside ''' is known as Docstring. It is very important in generative AI. 
"""

#Variables-- temporary storage of data during software running--named memory locations
#memory-- temporary storage- e.g, Ram, running of code is on RAM
#Storage-- Permanent storage
# We find the best container for data according to data in other languages. here python does it for us


# X: int=100 (-32768 to 32767)
# primitive data type
x=100 #integer
height=5.4 #float
name='umar' #string
disable=False #boolean
complx=3+2j #complex

#List
#Tuple
#Dictionaries
print('The value of height is ',height)

print('my name is: ',name, 'and my height is: ',height, 'disablity is ',disable)
# (F-string) to make it easier
print(f'my name is {name} and mmy height is {height} my disability is {disable}')
# Also called format string
print("my name is {0}, and my height is {1} and my disability is {2}".format(name,height,disable))

# type function

print ('the type of complex:', type( name))
# import numpy as np
# np1=np.array([1,2])
# print(np1)
# import pandas as pd
# pd1=pd.DataFrame({
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# })
# print(pd1)
# pd1['calories'][0]=804
# pd1.to_csv('pd1.csv')
# print(pd1)