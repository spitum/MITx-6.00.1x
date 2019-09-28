# Write a recursive Python function, given a non-negative integer N, to
# calculate and return the sum of its digits.
#
# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while
# doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
#
# This function has to be recursive; you may not use loops!
#
# This function takes in one integer and returns one integer.



def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here

    # If N < 9 then it has only one digit
    if N < 9:
        return N
    else:
        return ((N % 10) + sumDigits(N/10))

# Calling sumDigits, comment out before submitting
print(sumDigits(126))
print(sumDigits(123))
print(sumDigits(987))


# Write a Python function that returns a list of keys in aDict with the
# value target. The list of keys you return should be sorted in increasing
# order. The keys and values in aDict are both integers. (If aDict does not
# contain the value target, you should return an empty list.)
#
# This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Initialize matchList
    matchList = []
    for k,v in aDict.items():
        if v == target:
            matchList.append(k)
        
    return sorted(matchList)

# Calling keysWithValue(), comment out before submitting
# aDict{key : value, . . .}
aDict = {1 : 11, 2 : 22, 3 : 33, 5 : 44, 4 : 44}

print(keysWithValue(aDict, 11))
print(keysWithValue(aDict, 44))
print(keysWithValue(aDict, 77))


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    result = 0
    if base > num:
        result = 0
    elif base == num:
        result = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                result = i
                break
    return result


#For example,
closest_power(3,12) 
closest_power(4,12) 
closest_power(4,1) 


# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have
# the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is
# 1*4 + 2*5 + 3*6, meaning your function should return: 32

# Hint: You will need to traverse both lists in parallel.

# This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    new_list = []
    for i in range(len(listA)):
        mul = listA[i]*listB[i]
        new_list.append(mul)
    return sum(new_list)




listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA,listB))


# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also 
#     reverses the order of the int elements in every element of L. 
#     It does not return anything.
#     """
#     # Your code here
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

# Paste your function here
def deep_reverse(L):
    L_copy = []
    for s in L:
        L_copy.append(s[::-1])

    return L_copy

L = [[1, 2], [3, 4], [5, 6, 7]] 
print(deep_reverse(L))


# Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes
# in two integers, performs an unknown operation on them, and returns a value.

# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two
# dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:
# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect
# dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is
# the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f
# inside your dict_interdiff code -- assume it is defined outside.
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2
# or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.


# Here are two examples:
# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect  = {}
    difference = {}

    for k in d1:
        if k in d2:
            intersect[k] = (f(d1[k],d2[k]))
        else:
            difference[k] = d1[k]

    for k in d2:
        if k not in d1:
            difference[k] = d2[k]
    return (intersect,difference)

def f(a,b):
    return a > b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1,d2))




def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
    returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
    i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
   # Your code here
    L_copy = L[:]
    for i in L_copy:
        if (not g(f(i))):
            L.remove(i)
        if len(L) == 0:
            return -1
    return max(L)



# For example, the following functions, f, g, and test code:
def f(i):
    return i + 2
def g(i):
   return i > 5


L = [0, -10, 5, 6, -4, 7, 8, -2]
print(applyF_filterG(L, f, g))
print(L)
# Should print:6
#  [5, 6]
