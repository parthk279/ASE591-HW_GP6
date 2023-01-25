# from misc import *
# from row import ROW
# from col import COLS

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