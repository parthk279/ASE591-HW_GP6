import sys, re
from numerics import *
from config import *
from operator import itemgetter
import os


def csv(fileName, fun):
    """
        Calls the certain 'fun' on all the rows after moving through the cell text.

        Parameters
        ----------
        fileName : str : The Path of the csv file
        fun : function : Function that must be applied on ech row of the csv file
    """

    if os.path.exists(fileName) and fileName.endswith(".csv"):
        with open(fileName, "r", encoding="utf-8") as file:
            for _, row in enumerate(file):
                r = list(map(coerce, row.strip().split(",")))
                fun(r)
    else:
        print("File does not exist at : ", fileName)
        return 0


def misc(fun, iterable):
    """
    Maps the function over the iterable
    fun : Function that must be applied on each element of iterable
    iterable : iterable over which function must be mapped onto
    """
    u = []
    if iterable is None:
        return None
    elif fun is None:
        return u
    else:
        return [fun(i) for i in iterable]


def eg(key, str, fun):
    """
    Function for running the example test cases in test files and main.py
    """
    egs[key] = fun
    global help
    help = help + '  -g ' + key + '\t' + str + '\n'


def keys(t: dict):
    """
        Returns the sorted list of dictionary keys.
        t : dictionary
    """
    return sorted(t)


def fmt(*strings):
    """
        Emulating Print function for multiple string. It is very similar to the print() function in Python 3.x.

        Parameters
        ----------
        *strings : str - The string values that must be printed out.
    """
    for string in strings:
        string = str(string)
        for s in string:
            sys.stdout.write(s)


def oo(t):
    """
    Emulating Print function and returning sorted value
    """
    print(t)
    if not isinstance(t, dict):
        return t
    else:
        return dict(sorted(t.items(), key=itemgetter(1)))


def settings(s : str):
    """
        Coerces the global variables for the options. implements regular expression (regex) to refer to a sequence
        of characters that specifies a search patter in text. Used to find or find and replace operations for the
        global variables.

        Parameters
        ----------
        s : str - The value for which the regular expression must be implemented on.
    """
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))


def coerce(s):
    """
        This function is used to convert a value to a Boolean. When the input is not a boolean
        it converts it into a integer.

        Parameters
        ----------
        s : str - The value to be converted to a boolean or an integer.

        Returns
        ----------
        s : int or BOOL value of the input S.
    """
    if s == "true" or s == "True":
        return True
    elif s == "false" or s == "False":
        return False
    elif "." in s and s.replace('.', '').isdigit():
        return float(s)
    elif s.isdigit():
        return int(s)
    elif "." in s and s.replace(".", "").isdigit():
        return float(s)
    else:
        return s


def cli(options: dict):
    """
       Uses the command line interface to update "the" variable options from the command line.

       Parameters
       -----------
        options : dict : It is a dictionary containing the global variables and options.

        Returns
        ----------
        options : dict : The modified dictionary containing the updated globals options from the command line.
    """
    args = sys.argv[1:]
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(args):
            if x == "-" + k[0] or x == "--" + k:
                if v == "false":
                    v = "true"
                elif v == "true":
                    v = "false"
                else:
                    v = args[n + 1]
            options[k] = coerce(v)
        return options


Seed = 937162211


def rand(lo=0, hi=1):
    """
        This is a rudimentary implementation of the random function from the random module in Python 3.x.

        Parameters
        ----------
        lo : int : The lower bound of the range in which the random number must be generated from.
        hi : int : The higher bound of the range in which the random number must be generated from.

        Returns
        ---------
        float : A random number that lies between lo and hi.
    """
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647


def rint(lo, hi):
    """
        Implements the rand() function and returns the closest rounded off value of the float value generated
        between the two bounds lo and hi.

        Parameters
        ----------
        lo : int : The lower bound of the range in which the random number must be generated from.
        hi : int : The higher bound of the range in which the random number must be generated from.

        Returns
        ---------
        int : A random number that lies between lo and hi.
    """
    return round(0.5 + rand(lo, hi))


def rnd(n, nPlaces=3):
    """
        Takes a float number and rounds it off to three decimal places.

        Parameters
        ----------
        n : float : The number that must be rounded off to by n places.
        nPlaces : int : The number of places that the number must be rounded off to.
    """
    return round(n * (10 ** nPlaces) + 0.5) / (10 ** nPlaces)


def oo(t):
    """
        Emulating Print function and returning sorted value
    """
    print(t)
    if not isinstance(t, dict):
        return t
    else:
        return dict(sorted(t.items(), key=itemgetter(1)))


def kap(iterable, fun):
    """
        Applies a function over an iterable and returns the result as key value pair with key as index
        and value as result of the function

        Parameters
        ----------
        iterable : list : The iterable over which the function must be applied onto
        fun : function : the function that must be applied to the iterable

        Returns
        ----------
        result : dict : A key-value pair as index and result of the function
    """
    result = {}
    for i in iterable:
        index = iterable.index(i)
        i, index = fun(index, i)
        result[index or len(result)] = i
    return result


def push(t, x):
    t.append(x)
    return x


def any(iterable):
    """
        Returns random item from an iterable

        Parameters
        ---------
        iterable : list : The list from which the random item must be returned

        Returns
        -------
        A random item from the iterable
    """
    return iterable[rint(0, len(iterable) - 1)]


def many(iterable, n):
    """
        Returns a few items from an iterable

        Parameters
        ---------
        iterable : list : The list from which the items must be returned from
        n : The number of items that must be returned

        Returns
        -------
        list : A list of items randomly selected from the iterable
    """
    u = []
    for _ in range(1, n + 1):
        u.append(any(iterable))
    return u


def show(node, what, cols, nPlaces, lvl=0):
    """
        Prints the tree of the cluster

        Parameters
        ----------
        node : dict : The dictionary of the data to be printed
        what : str : The stat that must be returned - Either "mid" or "div"
        cols : COL : COl object to store the ROW
        nPlaces : int : Number of places to which the stats must be rounded to
    """
    if node:
        print('| ' * lvl + str(len(node['data'].rows)) + '  ', end='')
        if not node.get('left') or lvl == 0:
            print(node['data'].stats(node['data'].cols.y, nPlaces, "mid"))
        else:
            print('')
        show(node.get('left'), what, cols, nPlaces, lvl + 1)
        show(node.get('right'), what, cols, nPlaces, lvl + 1)
