import sys, re, copy, json
from numerics import *
from config import *
from operator import itemgetter
import os
import data
from sym import SYM
import math

def csv(fileName, fun):
    """
    Function for reading the csv file and applying a function over the text in csv file
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
    Returns the sorted list of dictionary keys
    t : dictionary
    """
    return sorted(t)


def fmt(*strings):
    """
    Emulating Print function
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


def settings(s):
    """
    Using REGEX to read the settings
    """
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))


def dofile(sFile):
    file = open(sFile, 'r', encoding='utf-8')
    text = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}', ']').replace('=',
                                                                                                        ':').replace(
        '[\n', '{\n').replace(' ]', ' }').replace('\'', '"').replace('_', '"_"')
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))


def coerce(s):
    """
    Reading the values in s and reformatting it for test use
    """

    def fun(s1):
        if s1 == "true" or s1 == "True":
            return True
        elif s1 == "false" or s1 == "False":
            return False
        return s1

    if s.isdigit():
        return int(s)
    elif "." in s and s.replace(".", "").isdigit():
        return float(s)
    else:
        return fun(s.strip())


def cli(options):
    """
    Function for displaying and for printing the command line interface options.
    """
    arg = sys.argv[1:]
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(arg):
            if x == "-" + k[0] or x == "--" + k:
                if v == "false":
                    v = "true"
                elif v == "true":
                    v = "false"
                else:
                    v = arg[n + 1]
            options[k] = coerce(v)

        return options


def kap(iterable, fun):
    """
    Applies a function over a iterable and returns the result as key value pair with key as index
    and value as result of the function
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
    """
    return iterable[rint(0, len(iterable) - 1)]


def many(iterable, n):
    """
    Returns a few items from an iterable
    """
    u = []
    for _ in range(1, n + 1):
        u.append(any(iterable))
    return u


def cosine(a, b, c):
    d = 1 if c == 0 else 2 * c
    w1 = (a ** 2 + c ** 2 - b ** 2) / d
    w2 = max(0, min(1, w1))
    y = abs((a ** 2 - w2 ** 2)) ** .5
    if isinstance(y, complex):
        print('a', a)
        print('x1', w1)
        print('x2', w2)
    return w2, y


def transpose(t):
    tt = []
    for i in range(len(t[1])):
        tt.append([])
        for j in range(len(t)):
            tt[i].append(t[j][i])
    return tt


def show(node, what, cols, n_places, lvl=0):
    """
    Prints the tree
    """
    if node:
        print('| ' * lvl + str(len(node['data'].rows)) + '  ', end='')
        if not node.get('left') or lvl == 0:
            print(node['data'].stats(node['data'].cols.y, n_places, "mid"))
        else:
            print('')
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


def extend(range, n, s):
    range['hi'] = max(n, range['hi'])
    range['lo'] = min(n, range['lo'])
    range['y'].add(s)


def value(has, nB=None, nR=None, sGoal=None):
    b, r = 0, 0
    sGoal, nB, nR = sGoal or True, nB or 1, nR or 1
    for x, n in has.items():
        if x == sGoal:
            b = b + n
        else:
            r = r + n
    b, r = b / (nB + 1 / float("inf")), r / (nR + 1 / float("inf"))
    return (b ** 2 / (b + r))


def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = {}
        for y, rows in rowss.items():
            for row in rows:
                x = row.cells[col.at]
                if x != "?":
                    k = int(bin(col, x))
                    if not k in ranges:
                        ranges[k] = RANGE(col.at, col.txt, x)
                    extend(ranges[k], x, y)
        ranges = list(dict(sorted(ranges.items())).values())
        r = ranges if isinstance(col, SYM) else mergeAny(ranges)
        out.append(r)
    return out


def bin(col, x):
    if x == "?" or isinstance(col, SYM):
        return x
    tmp = (col.hi - col.lo) / (the['bins'] - 1)
    return 1 if col.hi == col.lo else math.floor(x / tmp + .5) * tmp


def cliffsDelta(ns1, ns2):
    if len(ns1) > 256:
        ns1 = many(ns1, 256)
    if len(ns2) > 256:
        ns2 = many(ns2, 256)
    if len(ns1) > 10 * len(ns2):
        ns1 = many(ns1, 10 * len(ns2))
    if len(ns2) > 10 * len(ns1):
        ns2 = many(ns2, 10 * len(ns1))
    n, gt, lt = 0, 0, 0
    for x in ns1:
        for y in ns2:
            n = n + 1
            if x > y:
                gt = gt + 1
            if x < y:
                lt = lt + 1
    return abs(lt - gt) / n > the['cliffs']


def itself(x):
    return x


def merge(col1, col2):
    new = deepcopy(col1)
    if isinstance(col1, SYM):
        for n in col2.has:
            new.add(n)
    else:
        for n in col2.has:
            new.add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new


def merge2(col1, col2):
    new = merge(col1, col2)
    if new.div() <= (col1.div() * col1.n + col2.div() * col2.n) / new.n:
        return new


def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t)):
            t[j]['lo'] = t[j - 1]['hi']
        t[0]['lo'] = float("-inf")
        t[len(t) - 1]['hi'] = float("inf")
        return t

    ranges1, j = [], 0
    while j <= len(ranges0) - 1:
        left = ranges0[j]
        right = None if j == len(ranges0) - 1 else ranges0[j + 1]
        if right:
            y = merge2(left['y'], right['y'])
            if y:
                j = j + 1
                left['hi'], left['y'] = right['hi'], y
        ranges1.append(left)
        j = j + 1
    return noGaps(ranges0) if len(ranges0) == len(ranges1) else mergeAny(ranges1)


def RANGE(at, txt, lo, hi=None):
    return {'at': at, 'txt': txt, 'lo': lo, 'hi': lo or hi or lo, 'y': SYM()}


def showTree(node, what, cols, nPlaces, lvl=0):
    if node:
        print('|.. ' * lvl + '[' + str(len(node['data'].rows)) + ']' + '  ', end='')
        if not node.get('left') or lvl == 0:
            print(node['data'].stats("mid", node['data'].cols.y, nPlaces))
        else:
            print('')
        showTree(node.get('left'), what, cols, nPlaces, lvl + 1)
        showTree(node.get('right'), what, cols, nPlaces, lvl + 1)
