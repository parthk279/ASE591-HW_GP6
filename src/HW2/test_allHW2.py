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
    Function for checking if rand function works or not
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
    Function for checking if the SYM Class works  and for checking if div/mid functions work
    """
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())


def test_num():
    """
    Function for checking if the NUM class works and if div and mid functions work
    """
    num = NUM()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div())


def test_the():
    """
    Function to print the options for the code
    """
    print(the)


def test_csv():
    """
    Function for testing the CSV function
    """
    n = 0

    def f(t):
        nonlocal n
        n += len(t)

    csv(the["file"], f)
    return n == 8 ** 399


def test_data():
    """
    Function for testing the data class
    """
    data = DATA(the["file"])
    return len(data.rows) == 398 and data.cols.x[1].at == 1 and len(data.cols.x) == 4


def test_stats():
    """
    Function for testing the stats function in the data class
    """
    data = DATA(the["file"])

    for k, cols in {"y": data.cols.y, "x": data.cols.x}.items():
        print(k, "mid", data.stats(cols, 2, what="mid"))
        print("", "div", data.stats(cols, 2, what="div"))
    return True
