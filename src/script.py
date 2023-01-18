import math
import sys
from operator import itemgetter

#########################################################
#                                                       #
#                       CLASSES                         #
#                                                       #
#########################################################
class SYM:
    def __init__(self):
        """
        Constructor for SYM Class
        n : Count of symbols
        has : Dictionary with count
        most : Symbol with most number of entries
        mode : Number of entries of "most" symbol
        """
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = 0

    def add(self, newsym : str):
        """
        Takes a string symbol as argument and adds it to the SYM's "has" counter. If
        the new symbol is the one with most entries "mode" and "most" are modified
        """
        self.has[newsym] = 1+ self.has.get(newsym, 0)
        if self.has[newsym] > self.most:
            self.most = self.has[newsym]
            self.mode = newsym


    def mid():
        """
        Returns mode
        """
        return self.mode

    def div():
        """
        Returns the Shannon Entropy of the Object's counter "has"
        """
        freqlist = [i/sum(self.has.values()) for i in self.has.values()]
        entropies = [i*math.log(i, 2) for i in freqlist]
        entropy = -sum(entropies)
        return entropy


class NUM():
    def __init__(self):
        """
        Constructor for NUM Class
        count : To count number of entries
        mu : mean of all entered values
        m2 : Standard Deviation
        lo : lowest numerical entry
        hi : highest numerical entry
        """
        self.count, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = math.inf, -math.inf

    def add(self, n):
        """
        Function to add an entry to the NUM object.
        Recalculates mean (mu) and std dev (m2).
        """
        self.count += 1
        d = n - self.mu
        self.mu += d/self.count
        self.m2 += d*(n - self.mu)
        self.lo = min(self.lo, m)
        self.hi = max(self.hi, n)

    def mid(self):
        """
        Returns the mean (mu)
        """
        return self.mu

    def div(self):
        """
        Returns the Standard Deviation
        """
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2/(self.n-1))**0.5


#########################################################
#                                                       #
#                      NUMERICS                         #
#                                                       #
#########################################################

Seed = 937162211
def rand(lo = 0,hi = 1):
    """
    Retruns the float value x between lo and hi
    """
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647


def rint(lo, hi):
    """
    Returns the rounded off digit of a random float value between lo and hi
    """
    return math.round(0.5 + rand(lo, hi))

def rnd(n, nPlaces = 3):
    """
    Rounds off the digit to n number of places
    """
    return math.round(n*(10**nPlaces) + 0.5)/(10**nPlaces)


#########################################################
#                                                       #
#                       LISTS                           #
#                                                       #
#########################################################

def maping(fun, iterable):
    """
    Maps the function over the iterable
    fun : Function that must be applied on each element of iterable
    iterable : iterable over which function must be mapped onto
    """
    return [fun(i) for i in iterable]

### NEED TO DO KAP ###

### NEED TO DO SORT ###

def keys(t : dict):
    """
    Returns the sorted list of dictionary keys
    t : dictionary
    """
    return sorted(t)


#########################################################
#                                                       #
#                      STRINGS                          #
#                                                       #
#########################################################

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

### NEED TO DO O() ###

def coerce(s):
    def fun(s1):
        if s1 == "true" or s1 == "True":
            return True
        elif s1 == "false" or s1 == "False":
            return False
        return s1
    if s.isnumeric():
        return int(s)
    elif "." in s:
        return float(s)
    else:
        return fun(s.strip())
