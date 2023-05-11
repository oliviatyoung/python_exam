from function_3 import *

def test_function_3():
    string,k = 'ATGTCTGTCTGTA',2
    actual_output = linguistic_complexity(string,k)
    expected_output = 0.5
    assert actual_output == expected_output

def test_function_3_13():
    string,k = 'ATGTCTGTCTGTA',13
    actual_output = linguistic_complexity(string,k)
    expected_output = 1.0
    assert actual_output == expected_output

def test_function_3_1():
    string,k = 'ATGTCTGTCTGTA',1
    actual_output = linguistic_complexity(string,k)
    expected_output = 1.0
    assert actual_output == expected_output
    
def test_function_3_error():
    string,k = 'ATGTCTGTCTGTA',3
    actual_output = linguistic_complexity(string,k)
    expected_output = 50
    assert actual_output == expected_output