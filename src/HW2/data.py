from misc import *
from row import ROW
from col import COL


class DATA:
    def __init__(self, src):
        """
        Initializing function for data class object.
        A container for self.rows to be summarized in self.cols
        """
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for i in src:
                self.add(i)

    def add(self, t):
        """
        Add a new row and update the column headers
        """
        if self.cols:
            if isinstance(t, list):
                t = ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COL(t)

    def clone(self, init, data):
        """
        For cloning the DATA object with the same structure as init
        """
        data = DATA(self.cols.names)
        for x in self.rows or []:
            data.add(x)
        return data

    def stats(self, cols=None, nPlaces=None, what=None,):
        """
        Function for returning a certain attribute or certain stats 
        for a column in data
        """

        def fun(k, col):
            if what == "div":
                value = col.div()
            else:
                value = col.mid()

            return col.rnd(value, nPlaces), col.txt

        return kap(cols or self.cols.y, fun)
