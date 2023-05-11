#!/usr/bin/env python3

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

    dict = count_substrings(string,k)
print(dict)    
    
if __name__ == "__main__":
    string = sys.argv[1]
    k = int(sys.argv[2])
    print("The number of observed substrings is:",dict)
