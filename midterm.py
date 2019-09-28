#midterm_6001x.py
# problem_3

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if x < b:
        return 0
    return 1 + myLog(x/b,b)

print(myLog(15,3))


#Problem 4
# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

# This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    new_list = [s for s in aList if len(s) < 4]

    return new_list


aList = ['UqOw', 'JjheulbXL', 'Iz', '', 'I', 'bqPtMLXXfH', 'jIt', 'Xmnz', 'xipEHc']
print(lessThan4(aList))

#Probem 5

# Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.

# Here are some examples:

# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
# If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
# If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    freq = {}

    for k,v in d.items():
        freq.setdefault(v,[]).append(k)

    for k in freq:
        freq[k].sort()

    return freq

d = {8: 6, 2: 6, 4: 6, 6: 6} 
print(dict_invert(d))


#Problem 6
# Write a function to flatten a list. The list contains other lists, strings, or ints. 
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flat = []
    for item in aList:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

lst = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(lst))

# Problem 7
# Write a Python function called satisfiesF that has the specification below. 
# Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

    L_copy = L[:]
    for s in L_copy:
        if (not f(s)):
            L.remove(s)
    return len(L)

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a','a','ba']
print(satisfiesF(L))
print(L)
