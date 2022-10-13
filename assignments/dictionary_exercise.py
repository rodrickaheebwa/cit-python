# items() method
# returns a view object which contains the key-value pairs of the dictionary, as tuples in a list.
# returns a list of tuples (key-value pairs)

# update() inserts the a dictionary, or an iterable object with key value pairs to the dictionary.

# range() returns an immutable sequence of numbers
# that can be converted into a list, tuple, set
# Python's range() function returns or anycodings_for-loop generates a sequence. This is a anycodings_for-loop relatively advanced distinction which anycodings_for-loop usually won't be an issue for a novice. anycodings_for-loop In older versions of Python range() anycodings_for-loop built a list (allocated memory for it anycodings_for-loop and populated with with values) and anycodings_for-loop returned a reference to that list. This anycodings_for-loop could be inefficient for large ranges anycodings_for-loop which might consume quite a bit of anycodings_for-loop memory and for some situations where you anycodings_for-loop might want to iterate over some anycodings_for-loop potentially large range of numbers but anycodings_for-loop were likely to "break" out of the loop anycodings_for-loop early (after finding some particular anycodings_for-loop item in which you were interested, for anycodings_for-loop example).

# enumerate() function takes a collection (e.g. a tuple) and converts/returns it as an enumerate object
# and adds a counter as the key of the enumerate object
# enumerate(iterable, start)
# Enumerate returns an object that contains a counter as a key for each value within an object, making items within the collection easier to access.
# enumerate loops over a collection of data turning each item into a key(counter)-value(element) pair
# The Python enumerate function offers a more simplistic way to access and count items in a data collection.
# sets (unlike tuples, dictionaries and lists) are unordered and, therefore, more likely to be enumerated.
# for item in enumerate(some_iterable): print(item) will print key-value tuples, with key as a counter and value as the elements of our iterable
# in a similar way, converting the result of enumeration into a list will return a list of those tuples
# the enumerate function is best used on sets, since they are unordered



# (0:0,1:1)
D = dict() 
for x in enumerate(range(2)): 
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D)

# result
# D = {}
# create [(0,0), (1,1)]
# for first x: x = (0,0), x[0] = 0 x[1] = 0, D[0] = 0, D[7] = 0
# for second x: x = (1,1), x[0] = 1 x[1] = 1, D[1] = 1, D[8] = 1
# D = {0:0, 7:0, 1:1, 8:1}