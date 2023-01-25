from misc import *
from row import ROW
from col import COLS

class DATA:
    def __init__(self, src):
        """
        A container for self.rows to be summarized in self.cols
        """
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            csv(self, self.add)
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
            self.cols = COLS(t)

    def clone(self, init, data):
        """
        For cloning the DATA object with the same structure as init
        """
        data = DATA(self.cols.names)
        for x in self.rows or []:
            data.add(x)
        return data
