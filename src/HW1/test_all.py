from misc import *
from num import NUM
from numerics import *
from sym import SYM
from config import *
from main import *


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
