import math


class SYM:
    """
        The SYM class is used to describe a sequence of symbols. Implements various functions for returning the
        mode and entropy of the class object.
    """

    def __init__(self, at = None, txt = None):
        """
            The constructor for SYM Class.

            Data Members
            ------------
            n : int : Count of symbols.
            has : dict :  Dictionary with count.
            most : str : Symbol with the highest occurrences in the class object.
            mode : int : Number of entries of "most" symbol
            at : int : SYM position that defaults to 0
            txt : str : name of the object.
        """
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, newSym):
        """
            Takes in a  string symbol as argument and adds it to the SYM class object's entries. If
            the new symbol is the one with most entries "mode" and "most" are modified.

            Parameters
            ----------
            newSym : str : The string symbol that must be added and stored in the SYM class object
        """
        if not newSym == "?":
            self.n = self.n + 1
            self.has[newSym] = 1 + self.has.get(newSym, 0)
            if self.has[newSym] > self.most:
                self.most = self.has[newSym]
                self.mode = newSym

    def mid(self):
        """
            Returns the number of occurrences of the symbol with the highest occurrences.

            Returns
            -------
            mode : int : The number of occurrences of the symbol with the highest occurrences.
        """
        return self.mode

    def div(self):
        """
            Calculates and returns the Shannon Entropy of the SYM class object's. Shannon Entropy calculated using
            the following algorithm - https://onestopdataanalysis.com/shannon-entropy/

            Returns
            -------
            entropy : The Shannon Entropy of all the different symbols in the SYM class object.
        """
        freqList = [i / sum(self.has.values()) for i in self.has.values()]
        entropies = [i * math.log(i, 2) for i in freqList]
        entropy = -sum(entropies)
        return entropy

    def rnd(self, x, n):
        """
            Returns X for SYM class objects.
        """
        return x
