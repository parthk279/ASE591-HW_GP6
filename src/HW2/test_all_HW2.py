from misc import *
from num import NUM
from numerics import *
from sym import SYM
from config import *
from data import *
from main import *


    
def eg(key, str, fun):
    """
        Example function for running the test cases. Takes in key, string and function that needs to be tested
    """
    egs[key] = fun
    global help
    help = help + '  -g ' + key + '\t' + str + '\n'


def test_rand():
    """
       The test function for testing the environment variable SEED.

       Returns
       -------
       BOOL : Checks if the two means are same for the same seed and if the rounded off value o the means are correct.
    """
    n1, n2 = NUM(), NUM()
    global Seed
    Seed = the['seed']
    for i in range(1, 10 ** 3 + 1):
        n1.add(rand(0, 1))
    Seed = the['seed']
    for i in range(1, 10 ** 3 + 1):
        n2.add(rand(0, 1))
    m1, m2 = rnd(n1.mid(), 1), rnd(n2.mid(), 1)
    return m1 == m2 and .5 == rnd(m1, 1)


def test_sym():
    """
        Test function for testing the SYM class.

        Returns
        -------
        BOOL : Boolean value to check if the mode is "a" and if the Shannon entropy is equal to 1.379
    """
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())


def test_num():
    """
        Test function for the NUM class

        Returns
        -------
        BOOL : Boolean value to check if the mean of the numbers in the class is equal to 11/7 and if the standard
                deviation of the numbers is equal to 0.787.
    """
    num = NUM()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div())


def test_the():
    """
        The test function for loading all the environment variables.

        Returns
        -------
        dict : The dictionary containing all the environment variables

    """
    print(str(the))


def test_csv():
    """
        Testing if the csv function is drawing the input from the csv file

        Returns
        -------
        BOOl : checks if the number of characters/length of the file is equal to 8**399
    """
    global csv
    n = 0

    def f(t):
        nonlocal n
        n += len(t)

    csv(the["file"], f)
    return n == 8 ** 399


def test_data():
    """
        Testing function for checking if the data class is working or not

        Returns
        --------
        bool : Checks if DATA object has the correct number of rows, weights lengths, and locations for the columns
    """
    data = DATA(the["file"])
    return len(data.rows) == 398 and data.cols.x[1].at == 1 and len(data.cols.x) == 4


def test_stats():
    """
        Testing function for checking if the data.stats() function is working properly. Calculates the mid and
        the div for the two data from the csv file.
    """
    data = DATA(the["file"])

    for k, cols in {"y": data.cols.y, "x": data.cols.x}.items():
        print(k, "mid", data.stats(cols, 2, what="mid"))
        print("", "div", data.stats(cols, 2, what="div"))
    return True
