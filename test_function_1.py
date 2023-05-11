from function_1 import *

def test_function_1():
    string,k = 'ATGTCTGTCTGTA',2
    actual_output = count_substrings(string,k)
    expected_output = 6
    assert actual_output == expected_output

def test_function_1_5():
    string,k = 'ATGTCTGTCTGTA',5
    actual_output = count_substrings(string,k)
    expected_output = 6
    assert actual_output == expected_output

def test_function_1_1():
    string,k = 'ATGTCTGTCTGTA',1
    actual_output = count_substrings(string,k)
    expected_output = 4
    assert actual_output == expected_output

def test_function_1_error():
    string,k = 'ATGTCTGTCTGTA',2
    actual_output = count_substrings(string,k)
    expected_output = 50
    assert actual_output == expected_output