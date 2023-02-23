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


def test_theFun():
  print(str(the))

def test_copyFun():
    """
    Create a dictionary called "t1"
    """
    t1 = {'a': 1, 'b': {'c': 2, 'd': [3]}}

    """
    Create a deep copy of "t1" and store it in "t2"
    """
    t2 = deepcopy(t1)

    """
     Modify the value of the first element in the list "d" inside the dictionary "b" in "t2"
    """

    t2['b']['d'][0] = 10000
    """
     Print the contents of "t1" and "t2" before and after the modification
     """
    print('Before:', t1, '\nAfter:', t2)



def test_randFun():
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


def test_symFun():
    """
    Function for checking if the SYM Class works  and for checking if div/mid functions work
    """
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())


def test_numFun():
    """
    Function for checking if the NUM class works and if div and mid functions work
    """
    num = NUM()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div())


def test_theFun():
    """
    Function to print the options for the code
    """
    print(the)


def test_repColsFun():
    t = repCols(dofile(the['file'])['cols'], DATA)
    _ = list(map(oo, t.cols.all))
    _ = list(map(oo, t.rows))

def test_synonymsFun():
    data = DATA(the['file'])
    show(repCols(dofile(the['file'])['cols'], DATA).cluster(),"mid",data.cols.all,1)

def test_repRowsFun():
    t=dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    _ = list(map(oo, rows.cols.all))
    _ = list(map(oo, rows.rows))

def test_prototypesFun():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    show(rows.cluster(),"mid",rows.cols.all,1)

def test_positionFun():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    rows.cluster()
    repPlace(rows)

def test_everyFun():
    repgrid(the['file'], DATA)