import sys, re, copy, json
from numerics import *
from config import *
from operator import itemgetter
import os
import data
from pathlib import Path

def csv(fileName, fun):
    """
        Calls the certain 'fun' on all the rows after moving through the cell text.

        Parameters
        ----------
        fileName : str : The Path of the csv file
        fun : function : Function that must be applied on ech row of the csv file
    """

    if os.path.exists(fileName) and fileName.endswith(".csv"):
        with open(fileName, 'r', encoding='utf-8') as file:
            for _, line in enumerate(file):
                row = list(map(coerce, line.strip().split(',')))
                fun(row)
    else:
        print("File does not exist: ", fileName)
        return


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
    d = t.__dict__
    d['a'] = t.__class__.__name__
    d['id'] = id(t)
    d = dict(sorted(d.items()))
    print(d)


def settings(s: str):
    """
        Coerces the global variables for the options. implements regular expression (regex) to refer to a sequence
        of characters that specifies a search patter in text. Used to find or find and replace operations for the
        global variables.

        Parameters
        ----------
        s : str - The value for which the regular expression must be implemented on.
    """
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))


def dofile(sFile):
    file = open(sFile, 'r', encoding='utf-8')
    text = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))


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
    if s == 'true':
        return True
    elif s == 'false':
        return False
    elif s.isdigit():
        return int(s)
    elif '.' in s and s.replace('.', '').isdigit():
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
        for n, x in enumerate(args):
            if x == '-' + k[0] or x == '--' + k:
                if v == 'false':
                    v = 'true'
                elif v == 'true':
                    v = 'false'
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
    return 4 or math.floor(0.5 + rand(lo, hi))


def rnd(n, nPlaces=3):
    """
        Takes a float number and rounds it off to three decimal places.

        Parameters
        ----------
        n : float : The number that must be rounded off to by n places.
        nPlaces : int : The number of places that the number must be rounded off to.
    """
    return round(n * (10 ** nPlaces) + 0.5) / (10 ** nPlaces)


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


def cosine(a, b, c):
    """
        Get x, y from a line connecting `a` to `b`

        Parameters
        ----------
        a : float : The a value to calculate the cosine from
        b : float : The b value to calculate the cosine from
        c : float : The c value to calculate the cosine from

        Returns
        -------
        x : float : x from the line that connects a and b
        y : float : y from the line that connects a and b
    """
    den = 1 if c == 0 else 2 * c
    x1 = (a ** 2 + c ** 2 - b ** 2) / den
    x2 = max(0, min(1, x1))
    y = abs((a ** 2 - x2 ** 2)) ** .5
    if isinstance(y, complex):
        print('a', a)
        print('x1', x1)
        print('x2', x2)
    return x2, y


def transpose(t):
    u = []
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])
    return u


def show(node, what, cols, n_places, lvl=0):
    """
        Prints the tree

        Parameters
        ----------
        node : Node of the tree
        what : The Statistics that needs to be printed
        cols : Columns to print the statistics for
        n_places : Number of decimals
        lvl : Level in the tree
    """
    if node:
        print('|..' * lvl, end='')
        if not node.get('left'):
            print(node['data'].rows[-1].cells[-1])
        else:
            print(int(rnd(100 * node['c'], 0)))
        show(node.get('left'), what, cols, n_places, lvl + 1)
        show(node.get('right'), what, cols, n_places, lvl + 1)


def repPlace(data):
    n, g = 20, {}
    for i in range(1, n + 1):
        g[i] = {}
        for j in range(1, n + 1):
            g[i][j] = ' '
    maxy = 0
    print('')
    for r, row in enumerate(data.rows):
        c = chr(97 + r).upper()
        print(c, row.cells[-1])
        x, y = row.x * n // 1, row.y * n // 1
        maxy = int(max(maxy, y + 1))
        g[y + 1][x + 1] = c
    print('')
    for y in range(1, maxy + 1):
        print(' '.join(g[y].values()))


def deepcopy(t):
    return copy.deepcopy(t)


def repCols(cols, DATA):
    cols = deepcopy(cols)
    for col in cols:
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    first_col = ['Num' + str(k + 1) for k in range(len(cols[1]) - 1)]
    first_col.append('thingX')
    cols.insert(0, first_col)
    return DATA(cols)


def repRows(t, DATA, rows):
    rows = deepcopy(rows)
    for j, s in enumerate(rows[-1]):
        rows[0][j] = rows[0][j] + ":" + s
    rows.pop()
    for n, row in enumerate(rows):
        if n == 0:
            row.append('thingX')
        else:
            u = t['rows'][- n]
            row.append(u[len(u) - 1])
    return DATA(rows)


def repgrid(sFile, DATA):
    t = dofile(sFile)
    rows = repRows(t, DATA, transpose(t['cols']))
    cols = repCols(t['cols'], DATA)
    show(rows.cluster(), "mid", rows.cols.all, 1)
    show(cols.cluster(), "mid", cols.cols.all, 1)
    repPlace(rows)
