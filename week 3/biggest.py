def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    max_len = 0
    max_key = ""
    for key in aDict:
        cur_len = len(aDict[key])
        if cur_len>max_len:
            max_key = key
            max_len = cur_len
    return max_key
