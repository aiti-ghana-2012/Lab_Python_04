"""
Lab_Python_04
Extra Credit
Solutions for Extra Credit problem 5
"""

## Question A
# They should use a dictionary to keep track of which nodes
# have been seen. The dictionary should map the name of a
# node to a boolean indicating if that node has been seen.
# This allows for very fast and efficient lookup to check
# if a node has been seen or not, much faster than having to 
# walk through then entire list of nodes.

## Question B
# Which one will work faster depends on the structure of the
# Bus routes (the graph of nodes). This question is asking about
# The difference between breadth-first  and depth-first search.
# If you are curious, ask me or check it out on the internet to learn more.

## Question C
# A python Queue is a data structure that is highly optimized for addition
# and removal from either end, unlike a list, which is fast for additions
# and removals from only one end (the back, right side of it).
# John's strategy would benefit the most, because he uses to_visit
# As a queue, removing elements from the front, but adding them to the back.
# The Queue is a very common data structure, especially when building web
# And real-time applications that must handle many actions happening at once.
# If you ever find yourself adding elements to one end of a list, and removing
# Them from another, you may want to think about using a Queue. Again,
# please come see me, I would love to explain more or talk about other
# data structures (like a Stack, a Deque, Priority / heap queue, theres a lot!)

