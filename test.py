'''
print (7 * 7 * 24 * 60)

print (25+55)

print (299792458 * 100 * 1/1000000000)
'''

#Test of Debugging ex-1
'''
print (1)
print (2)
print (3)
print (4)
print (5)
print (6)
print (7)
print (8)
print (9)
'''
#Test of Debugging ex-2
'''
print (1)
print  (2)
print   (3)
print    (4)
print     (5)
print       (6)
print          (7)
print             (8)
print                (9)
'''

#Test of Debugging ex-3
'''
print (1)
print (2)
print (3)
print (4)
print (5)
Print (6)
print (7)
print (8)
print (9)
'''

#Test ex-4
'''
speed_of_light = 299792458
billionth = 1/1000000000
nanostick = speed_of_light *billionth * 100
cycles_per_second = nanostick / 2700000000
print (cycles_per_second)
'''
#Test ex-5 varying variables 1
'''
hours = 9
hours = hours + 1
hours = hours * 2
print (hours)
'''

#Test ex-6 ''
'''
minutes = minutes + 1
seconds = minutes * 60
print (seconds)
'''

#Test ex-7 define age in days
'''
age = 26 * 365
print (age)
'''

#Test ex-8 string
'''
name = "Yasir"
print ('Hello ' + name + '!')
'''

#Test ex-9 string + number
'''
name = "Yasir"
print ('Hello ' + name + '!' * 5)
'''

#Test ex-10
#Experimenting with Strings

#This code shows some basic variable assignment and string printing.
'''
name = "Yasir"
print ('Hello ' + name)
print (name * 4)
'''

# This code shows the difference between the string "4" and the number 4.
'''
print (4)
print ("4")
print (4 + 4)
print ("4" + "4")
'''

# This code shows some of the different mistakes that are easy to make while 
# working with strings. Remove one comment at a time and press Test Run to 
# see what happens. Be sure to re-comment before moving on or the program
# will keep showing you an error.

'''
print ('hello")
print (hello)
print ("hello)
'''

# This code will give you a peek at what you are about to learn! Uncomment 
# all of the lines below to get a glimpse of "string indexing"
'''
name = "Yasir"
print (name [0])
print (name [1])
print (name [2])
print (name [3])
print (name [4])
'''

#Test ex-11
# Write Python code that prints out Udacity (with a capital U)
'''
s = 'audacity'
print ('U' + s[2:])
'''

#Test ex-12 Practice with string.find()
'''
print ("Example 1: Finding substrings in a string")
print ("test".find("te"))
print ("test".find("st"))
print ("test"[2:])
print ("test"[1:])
print ("test"[:])
'''

#Test ex-13 Practice with string.find()
'''
print ("Example 2: Finding substrings in a string which is stored as a variable")
my_string = "test"
print (my_string.find("te"))
print (my_string.find("st"))
print (my_string[2:])
'''

#Test ex-14 Practice with string.find()
'''
print ("Example 3: Printing out everything after a certain substring")
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print (favorite_color) # opps, this line prints out 'color:' as well....
print (favorite_color[7:]) # this fixes it !
'''

#Test ex-15 Practice with string.find()
'''
print ("Example 4: Other interesting things about string.find()...")
print ("text".find("text")) # prints 0
print ("text".find("Text")) # prints -1
print ("text".find(""))     # prints 0
print ("text".find(" "))    # prints -1  
'''

#Test ex-15 Practice with string.find

'''
print ("Ex 1: using find to print the second occurrence of a sub-string") 
print ("test".find("t"))
print ("test".find("t, 1"))
'''
#Test ex-16 Practice with string.find
'''
print ("Example 2: using a variable to store first location")
first_location = ("consol".find("o")) # here we store the first location of "t"
print (first_location)
print ("consol".find("o", first_location+1)) # then we use that location to find the second occurrence.
'''

#Test ex-17 Practice with string.find
'''
print ("Example 3: using find to get rid of exclamation marks!!")
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print (new_string) # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print (new_string)
'''

# Python Programming 1

# Write Python code that prints out the number of hours in 7 weeks.

'''
print(7*7*24)
'''


# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious    # without using any quote characters in.
'''
print(s[0]+t[2:])

# Or this

print(s[:-2]+t[-3:])
'''

# String Slicing-19
'''
sentence = "A Noun went on a walk."
substring = sentence[6:]
print(substring)
'''

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.  ex20
'''
sentence = "A noun went on a walk. It can verb really fast."
substring1 = sentence[:2]
substring2 = sentence[6:29]
substring3 = sentence[34:]
print(substring1)
print(substring2)
print(substring3)
print(substring1+substring2+substring3)
'''

# String Concatenation ex21

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence. 
'''
sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "Apple" # your noun here
verb_replacement = "fall" # your verb here
new_sentence =""

new_sentence += substring1
new_sentence += noun_replacement
new_sentence += substring2
new_sentence += verb_replacement
new_sentence += substring3
print (new_sentence)
'''

# Variables 1 -ex22
# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".
'''
mary = "Mary"
randa = mary
katie = randa
salwa = katie
kathleen = salwa
gabriel = kathleen
print(gabriel)
'''

# Finding Strings ex23
'''
text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find("NOUN")
verb_position = text.find("VERB")

print(noun_position)
print(verb_position)
'''

#Find 2 ex24
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip' # in text, or -1 if it does not occur   # at least twice.
'''
text = "all zip files are zipped."
#text = "zip files are compressed"
code = text.find("zip")
print (text.find('zip',code+1))
'''

# Replacing Strings ex25
# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
'''
sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace("NOUN", "cat")
sentence = sentence.replace("VERB", "very")
print(sentence)
'''

