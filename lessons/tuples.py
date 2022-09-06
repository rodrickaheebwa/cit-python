# tuples
# to create a tuple with one element, add a comma e.g. (1,)
# isinstance() - to check if an item is a tuple, list etc
# we can delete a tuple but not its individual items


D = dict() 
for x in enumerate(range(2)):
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D)

# {0: 0, 7: 0, 1: 1, 8: 1}
# enumerate() will return a tuple, the loop will have x = (0, 0), (1, 1). Thus D[0] = 0, D[1] = 1, D[0 + 7] = D[7] = 0 and D[1 + 7] = D[8] = 1. Note: Dictionary is unordered, so the sequence of the key-value pair may differ in each output.