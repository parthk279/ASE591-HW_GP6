import sys, re, math
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
        self.mode = None

    def add(self, newSym):
        """
        Takes a string symbol as argument and adds it to the SYM's "has" counter. If
        the new symbol is the one with most entries "mode" and "most" are modified
        """
        if not newSym == "?":
            self.n = self.n + 1
            self.has[newSym] = 1 + self.has.get(newSym, 0)
            if self.has[newSym] > self.most:
                self.most = self.has[newSym]
                self.mode = newSym

    def mid(self):
        """
        Returns mode
        """
        return self.mode

    def div(self):
        """
        Returns the Shannon Entropy of the Object's counter "has"
        """
        entropy=0
        freqList = [i / sum(self.has.values()) for i in self.has.values()]
        entropies = [i * math.log(i, 2) for i in freqList]
        entropy = -sum(entropies)
        return entropy
