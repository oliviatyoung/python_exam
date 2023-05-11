#!/usr/bin/env python3

import sys


def possible_substrings(string,k):
    '''
    Count the number of observed substrings with length k
    
    Args:
        string (str) = sequence of letters ('DNA') in single quotation marks 
        k (int) = length of substring (integer) that is less than or equal to the lenth of the string
    
    Return:
        number of times the substrings with length k are observed in the string
    '''
    substrings_possible = {}
    n = len(string)
    if k<= n: # the substring length can't be greater than length of string
        return n-k+1 if k > 1 else 4 # calculates the possible strings, if the length is 1 then there are only 4 options because there are only 4 bases to chose from
    else:
        return 0 # if the length of substring deos not fit in the string, there are no possible substrings
    pos_substrings = possible_substrings(string,k)
    return substrings_possible


if __name__ == "__main__":
    string = sys.argv[1]
    k = int(sys.argv[2])

    print("The number of possible substrings is:",pos_substrings)