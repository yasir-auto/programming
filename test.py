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

# functions 

# A Taste of What You'll Learn Part 1 ex26
'''
def say_hello():
    return "Hello!"

print (say_hello())
'''
# A Taste of What You'll Learn Part 2 ex26
'''
def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

print (say_hello("khan"))
print (say_hello("asad"))
'''
# A Taste of What You'll Learn Part 3 ex26
'''
def add_two_number(number_1, number_2):
    return number_1 +   number_2

print (add_two_number(5, 8))
print (add_two_number(4, 7))
print (add_two_number(15, 8))

def subtract_two_number(number_1, number_2):
    return number_1 + number_2

print (subtract_two_number(4, 3))
'''

# Define a procedure, square, that takes one number ex26
'''
def sum(a, b):
    c = a+b
    return c

print (sum(5,6))


def square(a):
    return a*a

print (square(9))

# Sum of Three

def sum3(a,b,c):
    d = a+b+c
    return d

print (sum3(93,53,70))

def abbaize(a,b):
    return a+b+b+a

print (abbaize('dog','cat'))
'''

# Work Session: Print vs Return ex27
'''
def udacify(a):
    return "U"+a

print (udacify("dacians"))
print (udacify('turn'))
print (udacify('boat'))
'''

# Equality Comparisons ex28
'''
print ("Example 1: Greater-than and less-than comparisons")
print (2 > 1)
print (1 > 2)
print (5 < 20)
print (100 < 19)
'''
'''
print ("Example 2: Equality and non-equality comparisons")
print(5==5)
print ("hello"=="hello")
print(5==10)
print(5=='5') # what do you think will happen here?
print(7!=10)
print(7!=7)
'''
'''
print ("Example 3: A demo of what you are about to learn")
if 3<5:
    print("Three is smaller then 5!")

if 10>20:
    print("10 is gratter then 20!")
else:
    print("20 is greater than 10!")
'''

# If Statements ex29

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.
'''
def bigger(a,b):
    return max(a,b)

print (bigger(5,7))
print(bigger(10,5))
'''
# by own
'''
def bigger(a,b):
    if a>b:
        print('a'+ " is greater")
    else:
        print('b' + " is greater")
        
print(bigger(12,10))
'''
'''
def bigger(a,b):
    if a>b:
        return a
    else:
        return b
print(bigger(5,8))
print(bigger(8,4))
'''

# Is Friend ex30
'''
def is_friend(name):
    if name[0] == 'y':
        return True
    else:
        return False

print(is_friend("yasir"))
print(is_friend("khan"))
'''

# another way from OR
'''
def is_friend(name):
    return name[0] == 'y' or name[0] == 'k'

print(is_friend("yasir"))
print(is_friend("khan"))
'''

#Biggest quiz

'''
def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(biggest(5,8,11))
print(biggest(10,41,7))
'''

# While Loops ex31
'''
i=0
while i != 10:
    i = i+1
    print (i)
'''
# While Loops 2
'''
i=0
while i != 10:
    i = i+2 
    print (i)
'''

# While Loop Playground

# This code demonstrates a while loop with a "counting variable"

'''
i = 0
while i < 10:
    print (i)
    i = i+1
'''

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
'''
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text !='':
        next_character = text[0]
        if next_character != ' ':   #that a single space
            text_without_spaces =text_without_spaces +next_character
        text = text[1:]
    return text_without_spaces
print (remove_spaces("hello my name is khan how are you?"))
'''
# Print Numbers quiz

'''def print_number(a):
    i = 0
    while i < a:
        i= i+1
        print (i)
'''
'''
def  print_numbers(n):
    i = 0
    while(i <n):
        i+=1
        print(i)
    return

print(print_numbers(3))
'''

# Deep Debugging ex32

# A small change will fix the crashing bug in printInches.
'''
def printExample(a, b):
    print (a + b)
    
def printInches(n):
    print (str (n) + " inches")

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)
'''

# Strategy: Work from a Working Example

'''
def bracket(text):
    return '[' + text + ']'

def boldwrap(text):
    return '<b>' + text + '</b>'

print (boldwrap('This is an important message.'))
'''



# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

'''
def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location ==-1:
        return somestring 
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

# 
# Don't change these test cases!
print (remove('audacity', 'a'))
print (remove('pythonic', 'ic'))
print (remove('substring institution', 'string in'))
print (remove('ding', 'do'))  # "do" isn't in "ding"; should print "ding"
print(remove('doomy', 'dooming'))  # and this should print "doomy"
'''

# Work Session: Mad Libs Generator ex33

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

'''
def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False

print(weekend('Saturday'))
'''

# Blastoff
'''
def countdown(n):
    i = n
    while (i>0):
        print(i)
        i-=1
print(countdown(5))
print('Blastoff')
'''

# another way
'''
def countdown(n):
    while n>0:
        print(n)
        n=n-1

print(countdown(3))
print('Blastoff')
'''

# Median
'''
def bigger(a,b):
    if a > b:
        return a
    else:
        return b


def median(a,b,c):
    if bigger(a, b)<=c:
        return bigger(a , b)
    if bigger(a, c)<=b:
        return bigger(a, c)
    if bigger(c, b)<=a:
        return bigger (c ,b)

print(median(9,3,6))
'''

# Random Nouns

from operator import index
from random import randint
from typing import TextIO
'''
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"
print(random_noun())
'''
'''
def random_verb():
    a = randint(0,1)
    if a == 0:
        return "run"
    else:
        return "kayak"

print(random_verb())
'''

# Word Transformer
'''
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def random_verb():
    a = randint(0,1)
    if a == 0:
        return "run"
    else:
        return "kayak"

def word_transformer(word):
    if word == "noun":
        return random_noun()
    if word == "verb":
        return random_verb()
    else:
        return word[0]


print(word_transformer('verb'))
'''

                            #Process Mad Lib

'''
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def random_verb():
    a = randint(0,1)
    if a == 0:
        return "run"
    else:
        return "kayak"

def word_transformer(word):
    if word == "noun":
        return random_noun()
    if word == "verb":
        return random_verb()
    else:
        return word[0]

def process_madlib(madlib):
    processed = " "
    index= 0
    box_length= 4
    while index < len(madlib):
        frame = madlib[index : index + box_length]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add) == 1:
            index += 1
        else:
            index += 4
    return processed

test_string_1 = "This is a good noun to use when you verb your food"
test_string_2 = "I'm going to verb to the store and pick up a noun or two."

print (process_madlib(test_string_1))
print (process_madlib(test_string_2))
'''

# Experiment with Lists ex34

'''
print ("EXAMPLE 1: Lists can contain strings")
string_list = ['HTML', 'CSS', 'Python']
print (string_list)
'''
'''
print ("EXAMPLE 2: Lists can contain numbers")
number_list = [3.14159, 2.71828, 1.61803]
print (number_list)
'''
#########################################################################
'''
spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1
print(agent[2])
'''
'''
spy = [0,0,7]
def replace_spy(spy):
    spy[2]+=2
    return spy

print(replace_spy(spy))
'''
'''
p = [1,2]
p.append(3)
p = p + [4,5]
print (len(p))
'''
'''
p =[1,2]
q = [3,4]
p.append(q)
print (len(p))
'''
'''
def measure_udacity(list):
    count = 0
    for name in list:
        if name[0] == 'U':
            count+=1
        
    return count

#print (measure_udacity(['Dave','Sebastian','Katy']))

print (measure_udacity(['Umika','Umberto']))
'''
'''
def find_element(xlist, y ):
    w = ('worng number')
     
    i = 0 
    for item in xlist:
        
        if item == y:
            return i
        i+=1
        
    else:
        
        return w

print (find_element([1,2,3],4))

print (find_element(['alpha','beta'],'beta'))

'''     

##########################################################################

#print ('yasir yasir hussain hussain') 

'''
x = 6
y = 9
z = x+y
print(z)
'''
'''
def find_element(xlist, y):
    if y in xlist:
        return xlist.index(y)
    else:

        return -1

#print (find_element([1,2,3],2))

print (find_element(['alpha','beta'], 'beta'))
'''


# Every entry in the following list is itself a list
nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[1]

print ("What do you think this will print?")
print (first_concept)


print ("Since first_concept was itself a list, we can access its elements")
first_title = first_concept[0]
first_description = first_concept[1]

print ("What will this print?")
print (first_title)
print (first_description)