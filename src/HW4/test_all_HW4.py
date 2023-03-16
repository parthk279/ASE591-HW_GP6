from misc import *
from num import NUM
from numerics import *
from sym import SYM
from config import *
from data import *
from main import *






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


def test_copy():
    t1 = {"a": 1,"b": {"c": 2, "d": [3]}}
    t2 = deepcopy(t1)
    t2["b"]["d"][0] = 10000
    print("b4", t1, "\nafter", t2)


