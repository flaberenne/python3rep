
#Let's start with something basic : text manipulation
txt='Hello World'
# write the string
print("-> write the string")
print(txt)
# get the first character
print("\n-> get the first character")
print(txt[0])
print(txt[:1])
# get the last character
print("\n-> get the last character")
print(txt[-1:])
# get the string without the last character
print("\n->get the string without the last character")
print(txt[:-1])
# get the string without the last character
print("\n-> get the string without the last character")
print(txt[1:])
# write the text by step of 2 characters starting from the 1st (index 0)
print("\n-> write the text by step of 2 characters starting from the 1st (index 0)")
print(txt[0::2])
# write the text by step of 2 characters starting from the 2nd (index 1)
print("\n-> write the text by step of 2 characters starting from the 2nd (index 1)")
print(txt[1::2])
# write reversed text
print("\n->  write reversed text")
print(txt[::-1])
# write in reverse by steps of 2 starting from 1st
print("\n->  write in reverse by steps of 2 starting from 1st")
print(txt[::-2])
# write in reverse by steps of 2starting from 2nd 
print("\n->  write in reverse by steps of 2 starting from 2nd")
print(txt[-2::-2])
