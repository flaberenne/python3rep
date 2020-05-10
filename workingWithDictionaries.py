"""
Working with dictionaries in python
https://github.com/flaberenne/python3rep/textManipulation.py
Author:flaberenne
"""
#Building a dictionary from 2 lists, the 1st one define the keys, the 2nd the values
a=['en','fr','br','es']
b=['Hello','Bonjour',"Bom dia","Buenos dias"]

dictionary={i:j for (i,j) in zip(a,b) }
print(dictionary)