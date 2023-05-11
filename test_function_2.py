from function_2 import *

def test_function_2():
    string,k = 'ATGTCTGTCTGTA',2
    actual_output = possible_substrings(string,k)
    expected_output = 12
    assert actual_output == expected_output

def test_function_2_13():
    string,k = 'ATGTCTGTCTGTA',13
    actual_output = possible_substrings(string,k)
    expected_output = 1
    assert actual_output == expected_output

def test_function_2_14():
    string,k = 'ATGTCTGTCTGTA',14
    actual_output = possible_substrings(string,k)
    expected_output = 0
    assert actual_output == expected_output

def test_function_2_error():
    string,k = 'ATGTCTGTCTGTA',2
    actual_output = possible_substrings(string,k)
    expected_output = 50
    assert actual_output == expected_output
