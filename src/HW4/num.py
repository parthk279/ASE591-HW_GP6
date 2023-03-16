import math
from numerics import *


class NUM:
    """
        The NUM class is used to provide a description for a series of numbers.
    """

    def __init__(self, at=None, txt=None):
        """
            The constructor  for NUM Class.

            Data Members
            ------------
            n : float : the value to be entered with NUM class.
            count : int : To count number of entries.
            mu : float : mean of all entered values.
            m2 : float :Standard Deviation.
            lo : float : lowest numerical entry.
            hi : float : highest numerical entry.
        """
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.n = 0
        self.count, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = math.inf, -math.inf
        self.w = -1 if "-" in self.txt else 1

    def add(self, n):
        """
            Adds an entry to the num class and updates the data members - lo, hi, mu (mean) and m2 (standard
            deviation) based on the newly added entry to the NUM class object.

            Parameters
            ----------
            n : float : The newly entered numerical value to be updated into the num class.

            Returns
            ---------
            NUM class object.
        """
        if n != "?":
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(self.lo, n)
            self.hi = max(self.hi, n)
        return self

    def mid(self):
        """
            Calculates the mean and returns the value based on entries in the NUM class.

            Returns
            -------
            self.mu : float : Mean value
        """
        return self.mu

    def div(self):
        """
            Calculates the standard deviation and returns the value based on entries in the NUM class. The algorithm
            implemented  - https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm

            Returns
            --------
            float : Standard deviation of all entries in the NUM Class.
        """
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def rnd(self, x, n):
        """
            Returns the value x if x is "?". Else it returns the closest rounded value of x rounded to n places

            Parameters
            ----------
            x : float : the value to be rounded off to
            n : int : the number of places to be rounded off to
        """
        if x == "?":
            return x
        else:
            return rnd(x, n)

    def norm(self, n):
        return n if n == "?" else (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1, n2):
        if n1 == "?" and n2 == "?":
            return 1
        n1, n2 = self.norm(n1), self.norm(n2)
        if n1 == "?":
            n1 = 1 if n2 < 0.5 else 0
        if n2 == "?":
            n2 = 1 if n1 < 0.5 else 0
        return abs(n1 - n2)
