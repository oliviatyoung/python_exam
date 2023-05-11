# Python Exam
This repository contains code to analyze strings of DNA and determine the linguistic complexity (how many observed substrings there are compared to the possible substrings there are) for each substring length

## Files in this repository
function_1.py: Counts the observed substrings in the string of a given length (k)
test_function_1.py: Test cases for function 1 (the last test is supposed to fail)

function_2.py: Counts the possible substrings in the string of a given length (k)
test_function_2.py: Test cases for function 2 (the last test is supposed to fail)

function_3.py: Calculates the linguistic complexity for the given substring length in the string
test_function_3.py: Test cases for function 3 (the last test is supposed to fail)

## Instructions for python_exam.py
#### This is the function to be used on the command line
There are 3 different functions in this script. The first one gives the observed number of substrings, the second one gives teh possible number of substrings, and the third calculates the linguistic complexity.

To use these functions, you must first clone the repository.

To use on the command line, make sure you are in the folder with the script, then type "python python_exam.py" followed by the DNA string you would like to analyze and the substring length you would like to use

Example:
    python python_exam.py ATGTCTGTCTGTA 2

This will return all 3 functions; function 1 on the top, function 2 in the middle, and function 3 on the bottom
