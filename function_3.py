#!/usr/bin/env python3

from __future__ import division #this is here to make sure the linguistic complexity shows up as a decimal on the command line

import sys

#get the observed number of substrings of a given length
def count_substrings(string,k): #make the function to count the substrings with the length of k (in this case k is 2)
    '''
    Count the number of observed substrings with length k
    
    Args:
        string (str) = sequence of letters ('DNA') in single quotation marks 
        k (int) = length of substring (integer) that is less than or equal to the lenth of the string
    
    Return:
        number of times the substrings with length k are observed in the string
    '''
    substring_dict = {} #make a dictionary for the substrings
    for i in range(len(string) - k+1): #use len to get the length of the string, not just the letters themselves
        substring = string[i:i+k] #substring goes from the starting point to however long the substring is
        if substring in substring_dict:
            substring_dict[substring] += 1 #if substring appears more than once, add it to the existing count
        else:
            substring_dict[substring] = 1 #if substring only appears once, the count is only 1      
    #substrings_set = set(count_substrings(string,k)) #collect the substrings that have the length of k
    #number_substrings = len(substrings_set) #counts the number of substrings that have the length of k (from substrings_set)
    return len(substring_dict)

    observed = count_substrings(string,k)


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


def linguistic_complexity(string,k):
    '''
    Calculate the linguitic complexity for the given substring length
    
    Arg:
        string (str) = sequence of letters ('DNA') in single quotation marks 
        k (int) = length of substring (integer) that is less than or equal to the lenth of the string
    
    Return:
        (float) linguitic complexity (observed substrings divided by possible substrings) for each given substring length
    
    '''
    ling_comp = float(count_substrings(string,k))/float(possible_substrings(string,k))
    return ling_comp
    #observed = count_substrings(string,k)
    #pos_substrings = possible_substrings(string,k)
    print("The linguistic complexity is:",ling_comp)

if __name__ == "__main__":
    string = sys.argv[0]
    k = int(sys.argv[1])