import math
import sys, random
from utils import *;
class NUM:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
    def add(self,n):
        if(n!="?"):
            self.n  = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n - self.mu)
            self.lo = math.min(n, self.lo)
            self.hi = math.max(n, self.hi)
        return self
    def mid(self):
        return self.mu
    def div(self):
        if(self.m2 <0 or self.n < 2):
            return 0
        else:
            return self.m2/(self.n-1)^0.5
         