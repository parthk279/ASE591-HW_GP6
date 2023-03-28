import math
from misc import rnd
from config import the


class NUM:
    def __init__(self, at=None, txt=None):
        """
        Constructor for NUM Class
        count : To count number of entries
        mu : mean of all entered values
        m2 : Standard Deviation
        lo : lowest numerical entry
        hi : highest numerical entry
        """
        self.at = at
        self.txt = txt
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = float('inf')
        self.hi = float('-inf')
        
        self.has = {}
        

    def add(self, n):
        """
        Function to add an entry to the NUM object.
        Recalculates mean (mu) and std dev (m2).
        """
        if n != "?":
            self.n += 1
            if self.n <= the['Max']:
                self.has[n]= n
            self.n += 1
            if self.n <= the['Max']:
                self.has[n]= n
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.sd =  0 if self.n<2 else (self.m2/(self.n - 1))**.5
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
          
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
            return (self.m2 / (self.n - 1)) ** 0.5

    def rnd(self, x, n):
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
