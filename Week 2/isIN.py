def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    aStr = aStr.lower()
    aStr = ''.join(sorted(aStr))
    if len(aStr) == 0:
        return False
    if len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        new_str = aStr[:len(aStr)//2]
        return isIn(char,new_str)
    elif char > aStr[len(aStr)//2]:
        new_str = aStr[len(aStr)//2:]
        return isIn(char,new_str)
