from misc import *
from num import NUM
from sym import SYM
from data import DATA

def test_the():
    """
        The test function for loading all the environment variables.

        Returns
        -------
        dict : The dictionary containing all the environment variables

    """
    print(str(the))

def test_copy():
    """
        The test function for copy(). Creates a deep copy and prints both the original
        and the copy.

        Returns
        ------
        Original dictionary and copy.
    """
    t1 = {"a": 1, "b": {"c": 2, "d": [3]}}
    t2 = deepcopy(t1)
    t2["b"]["d"][0] = 10000
    print("b4", t1, "\nafter", t2)

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

def test_repCols():
    """
        The test function for repCols().
    """
    t = repCols(dofile(the['file'])['cols'], DATA)
    for row in t.cols.all:
        oo(row)
    for row in t.rows:
        oo(row)


def test_repRows():
    """
        Test function for repRows()
    """
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))

    for row in rows.cols.all:
        oo(row)
    for row in rows.rows:
        oo(row)

def test_synonyms():
    """
        Test function for checking if synonyms exist.
    """
    data = DATA(the['file'])
    show(repCols(dofile(the['file'])['cols'], DATA).cluster(), "mid", data.cols.all, 1)

def test_prototypes():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    show(rows.cluster(),"mid",rows.cols.all,1)

def test_position():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    rows.cluster()
    repPlace(rows)

def test_every():
    repgrid(the['file'], DATA)