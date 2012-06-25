"""
Lab_Python_04
Solutions for Questions 1 - 3
"""

## Question 1
print "Question 1:"

groceries = ['bananas', 'strawberries', 'apples', 'bread']

print "Initial list:"
print groceries

# a.
groceries.append('champagne')

print "After appending 'champagne':"
print groceries

# b.
groceries.remove('bread')

print "After removing 'bread':"
print groceries

#c.

# John should make a dictionary
# that maps each food item to the aisle in which it can be found
food_aisle_map = {}
for food_item in groceries:
	# [0] gets the first character of a string
	# and lower() converts it to lowercase
	aisle = food_item[0].lower()
	food_aisle_map[food_item] = aisle 


## Question 2
print
print "Question 2:"

#a. 
# A dictionary should be used because it provides
# a way to map from an item to its price

#b.
catalogue = {
		'apples' : 7.3,
		'bananas' : 5.5,
		'bread' : 1.0,
		'carrots' : 10.0,
		'champagne' : 20.90,
		'strawberries' : 32.6
	    }

print "The catalogue:"
print catalogue


#c.
catalogue['strawberries'] = 63.43
print "After changing price of strawberries: "
print catalogue

#d.
catalogue['chicken'] = 6.5
print "After adding chicken:"
print catalogue



## Question 3
print
print "Question 3:"

#a.
# The data structure that is best for this is a list,
# because it is a good way to keep track of multiple items

#b.
# The method .keys() returns a list of dictionaries keys
in_stock = catalogue.keys()

#c.
# Tuples are sequences that are immutable - they cannot change
# You can convert a list to a tuple using the tuple() function
always_in_stock = tuple(in_stock)

#d.
print "Come To shoprite! We always sell:"

# you can iterate through a tuple just like through a list
for item in always_in_stock:
	print item

