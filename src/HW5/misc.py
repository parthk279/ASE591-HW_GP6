import sys, re
from numerics import *
from config import *
from operator import itemgetter
import os


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
    text  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
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
    n,g = 20,{}
    for i in range(1, n+1):
        g[i]={}
        for j in range(1, n+1):
            g[i][j]=' '
    maxy = 0
    print('')
    for r,row in enumerate(data.rows):
        c = chr(97+r).upper()
        print(c, row.cells[-1])
        x,y= row.x*n//1, row.y*n//1
        maxy = int(max(maxy,y+1))
        g[y+1][x+1] = c
    print('')
    for y in range(1,maxy+1):
        print(' '.join(g[y].values()))

# Define a function that merges two columns of data and returns the result
def merge(col1, col2):
    
    # Make a deep copy of the first column
    new = deepcopy(col1)
    
    # If the first column is of type SYM, add all the values from the second column
    # to the new column
    if isinstance(col1, SYM):
        for n in col2.has:
            new.add(n)
    # If the first column is of type NUM, add all the values from the second column
    # to the new column and update the range of values
    else:
        for n in col2.has:
            new.add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    
    # Return the new merged column
    return new


def RANGE(at,txt,lo,hi=None):
    return {'at':at,'txt':txt,'lo':lo,'hi':lo or hi or lo,'y':SYM()}

def mergeAny(ranges):
    # Helper function to remove gaps between ranges
    def noGaps(ranges):
        for i in range(1, len(ranges)):
            ranges[i]['lo'] = ranges[i-1]['hi']
        ranges[0]['lo'] = float("-inf")
        ranges[-1]['hi'] = float("inf")
        return ranges

    # Create a new list of merged ranges
    merged_ranges = []
    i = 0
    while i < len(ranges):
        # Get the current range and its right neighbor (if any)
        current_range = ranges[i]
        right_neighbor = None if i == len(ranges)-1 else ranges[i+1]

        # Merge the current range with its right neighbor if they overlap
        if right_neighbor is not None:
            merged_y = merge2(current_range['y'], right_neighbor['y'])
            if merged_y:
                current_range['hi'] = right_neighbor['hi']
                current_range['y'] = merged_y
                i += 1

        # Append the current range (possibly merged) to the list of merged ranges
        merged_ranges.append(current_range)
        i += 1

    # Return the merged ranges with no gaps
    if len(ranges) == len(merged_ranges):
        return noGaps(ranges)
    else:
        return mergeAny(merged_ranges)

# Define a function that merges two columns of data and returns the result
def merge2(col1, col2):
    
    # Merge the two columns into a new column
    new = merge(col1, col2)
    
    # Check if the variance of the new column is less than or equal to
    # the weighted average of the variances of the original columns
    if new.div() <= (col1.div() * col1.n + col2.div() * col2.n) / new.n:
        
        # If the condition is true, return the new merged column
        return new
