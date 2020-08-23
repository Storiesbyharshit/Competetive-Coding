#Python 3

''' Function to return total number of binary
    substrings in the given string.
    n: Length of string
    s: Given string
'''

def binarySubstring(n,s):
    number_of_ones=s.count('1')
    return ((number_of_ones*(number_of_ones-1))//2)
