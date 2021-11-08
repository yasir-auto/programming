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

print(s[0]+t[2:])

# Or this

print(s[:-2]+t[-3:])

