# Lua to Python Decoder Homework 3
This repo is the submission for the third homework for the CSC591 Special Topics in Computer Science : Automated Software
engineering course. Within this repo a team of 4 aim to implement the latest and best software 
engineering practices to convert certain code from Lua to Python. Each Homework submissions
builds on top of the previous homework. Therefore, the functionality of classes in each 
homework would just increase as time moves.   

We will now delve into each file and understand the functions implemented in each class. 


## `col.py`
This script includes the implementation of the `COL` class. The `COL` class is used for storing and dealing with NUM 
and SYM type objects. 

## `config.py`
This file contains some important environment variables required to implement the 
functionality of all the classes in the homework.

## `data.py`
The script for implementing `DATA` class. The `DATA` class acts as a container for the information in 
ROW type objects but is summarized in the form of COL type objects.

## `main.py`
The main file is contains all the code to run the test functions. It coerces through 
the environment variables to find the system arguments and then stress tests all the 
various function that have been implemented in this certain homework. The tests
are explained in more detail under the `test_all.py` file.

## `misc.py`
There do exist some miscellaneous functions that need to be implemented however, they cannot 
be part of any class. Therefore, this file `misc.py` was created, which contains multiple functions 
for implementing the various tests across the homework. 

## `num.py`
This script contains the complete implementation of the `NUM` class as of Homework 1. The `NUM` class is used
to hold and describe/summarize a stream of numerical values. As of Homework 1 there are three functions - `add` - to add 
a new entry into the NUM class, `mid` to calculate the mean of all entries, `div` to calculate the standard deviation 
of all entries. 

## `numerics.py`
Similar to the `misc.py` file except contains some functionality mainly concentrated for numeric values. Implement
functions majorly for getting the random values. 

## `sym.py`
This file contains the code implementation of the `SYM` class object as of Homework 1. The `SYM` class object is used
to hold and describe/summarize a stream of character symbols. The functionality is similar to that of the 
`NUM` class however the `mid` function is replaced by the `mode` function that returns the 
symbol with the highest occurrences in the object and the `div` function calculates the Shannon  
Entropy instead of the standard deviation. 

## `test_all.py`
Finally, the test file that is used to stress test and check if all the functions have been implemented correctly
for homework 1. The various functions are
1. test_the : The test function for loading all the environment variables. 
2. test_rand : The test function for testing the environment variable SEED.
3. test_sym : Test function for testing the SYM class.
4. test_num : Test function for the NUM class. 
5. test_stats : Testing function for checking if the data.stats() function is working properly. 
Calculates the mid and the div for the two data from the csv file
6. test_data : Testing function for checking if the data class is working or not
7. test_csv : Testing if the csv function is drawing the input from the csv file
