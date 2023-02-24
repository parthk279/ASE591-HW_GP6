import sys, re, math
class NUM:
    """
        The NUM class is used to provide a description for a series of numbers.
    """
    def __init__(self):
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
        self.n = 0
        self.count, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = sys.maxsize, -sys.maxsize

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

