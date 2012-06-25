"""
Lab_Python_04
Extra Credit
Solution to Extra Credit problem 4
"""


## Part A
# The right data structure to store the different market prices
# would be a dictionary whose keys are food items, and values
# either a list of prices, or another dictionary that maps
# the names of different stores to the price that they offer
# for example

multi_price_with_store_names  = {
					'bread' : {
							'shoprite' : 4.5,
							'maxi-mart' : 5.0,
							'r-link' : 0.5
						  },
					'water' : {
							'shoprite' : 0.9,
							'maxi-mart' : 0.8,
							'r-link' : 0.5
						  }
				}

# or...
multi_price_without_store_names = {
					'bread' : [
							4.5,
							5.0,
							0.5
						  ],
					'water' : [
							0.9,
							0.8,
							0.5
						  ]
				  }

# ultimately, what you need to do with the data will determine which data structure
# is better to use.


## Part B
# Binary Search
# Binary search insertion is very difficult to get right
# and it was awesome that some of you did it!
def binary_insert(new_float, some_list_of_floats):
	"""
	Binary Search works when inserting or searching through
	a sorted list. It works by repeatedly cutting the search
	space in half, until you find the place for which you look.

	It is similar to looking up a word in a dictionary.
	First, you open up half way, then check if the word you seek
	is before or after a word on that page. If it is after, you
	go to the middle of the second half of the dictionary,
	and if it is before, you go to the middle of the first
	half of the dictionary. This process repeats until you have
	found the definition.

	If you have questions about this algorithm or algorithms in
	general, I love to talk about them, and would definitely
	like to chat about algorithms, searching, sorts, runtime,
	et cetera!
	
	Also, this problem is notoriously hard to do correctly,
	so if you notice a bug in the code please let me know!!
	"""

	# upper and lower are variables that bound the range
	# of the list in which we are searching

	# initially, we are searching the whole list,
	# so upper is the last element, and lower is 0, the first
	upper = len(some_list_of_floats) - 1
	lower = 0
	
	# mid is the middle of the range 
	mid = (upper + lower) / 2

	# checking for corner solutions
	# if the input list is empty
	if upper == -1:
		some_list_of_floats.append(new_float)
		return

	# (when the new element is bigger or smaller than every other one)
	if new_float <= some_list_of_floats[lower]:
		# then we want to insert it before that element
		some_list_of_floats.insert(lower, new_float)
		return
	elif new_float >= some_list_of_floats[upper]:
		#then we want to insert it after that element
		some_list_of_floats.insert(upper + 1, new_float)
		return


	#while our range contains elements...
	while upper - lower > 0:
		
		if new_float < some_list_of_floats[mid]:
			# then we want to look at the left half
			upper = mid
		
		elif new_float > some_list_of_floats[mid]:
			# then we want to look at the right half
			# the plus one is important, because when
			# we find out mid, we round down
			lower = mid + 1
		
		else:
			# then new_float is equal to the middle one,
			# so we can insert it on either side
			some_list_of_floats.insert(mid,new_float)
			return
		
		mid = (upper + lower) / 2

	#ok, when we are here, we have found the spot!
	some_list_of_floats.insert(lower,new_float)
	return


## Part C
# finding the min cost
# this problem is not so tricky once you see
# the the minimum cost is the sum of the minimum costs
# for each item. The hard thing is understanding
# and working with the given data structures
def min_cost(grocery_list, item_to_price_list_dict):
	
	total_cost = 0
	
	for item in grocery_list:
		# for each item, we want to get the minimum
		# price out of all of them
		
		# first, get the list of prices for this item
		list_of_prices = item_to_price_list_dict[item]
		
		# then, find the minimum
		# python has a convenient min() function which
		# takes a list and returns the smallest element
		lowest_price_for_item = min(list_of_prices)
		
		# now we add it to our running total of cost
		total_cost += lowest_price_for_item
		
	return total_cost





