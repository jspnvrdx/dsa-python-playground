# Playground for array/list methods

array = [1, 2, 3, 5]

# [1, 2, 3, 5]
array.append(5)  # Will append an element at the end of the list

# Returns a copy of specified list
# Same output as `copyarray = array`
copyarray = array.copy()
print("array:", copyarray)

# returns the number of times the value 5 appears in the list
print("count:", array.count(5))

newarray = [10, 9, 8]

# adds another list elements to the end of the current list
array.extend(newarray)
print(f"\narray and newarray extended: {array}")

# returns the index at the first occurrence of the specified value
# current array: [1, 2, 3, 5, 5, 10, 9, 8]
# 5 is found first at index 3
print('index of "5":', array.index(5))

# inserts specified value at the specified index position
array.insert(0, "hello")
print(array)

# removes the specified element at the specified position
array.pop(1)
print(array)

# removes the first occurence of the element with the specified value
array.remove("hello")
print(array)

# Reverses the order of the lists
array.reverse()
print(array)

# -----------------------------------------------
# ARRAY sort()

# Sorts the list
array.sort()
print(array)

# sorts the list reversely
array.sort(reverse=True)
print(array)

# sorts using key parameter
# key is a function to specify the sorting criteria/s

words = ["This", "is", "Python"]


# returns the length of the value
def myFunc(e):
    return len(e)


words.sort(reverse=True, key=myFunc)
print(words)
# -----------------------------------------------

# removes all elements from the list
array.clear()
print("cleared array:", array)
