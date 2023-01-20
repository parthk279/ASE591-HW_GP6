import sys, re, math
class NUM:
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
        if n != "?":
            self.count += 1
            d = n - self.mu
            self.mu += d / self.count
            self.m2 += d * (n - self.mu)
            self.lo = min(self.lo, n)
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
            return (self.m2 / (self.n - 1)) ** 0.5

