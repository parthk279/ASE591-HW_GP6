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

def stats(self, what = None, cols = None, nPlaces = None):
    """
    Function for returning a certain attribute or certain stats 
    for a column in data
    """
    def fun(k, col):
      return round(getattr(col, what or "mid")(col), nPlaces), col.txt
    return [fun(k, col) for k, col in enumerate(cols or self.cols.y)]
