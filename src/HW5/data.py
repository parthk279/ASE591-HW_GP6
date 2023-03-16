from misc import *
from row import ROW
from col import COL
from config import *
from numerics import *
import math
import misc


class DATA:
    def __init__(self, src):
        """
        Initializing function for data class object.
        A container for self.rows to be summarized in self.cols
        """
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            misc.csv(src, self.add)
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

    def clone(self, init={}):
        """
        For cloning the DATA object with the same structure as init
        """
        data = DATA([self.cols.names])
        for x in self.rows or []:
            data.add(x)
        return data

    def stats(self, cols=None, nPlaces=None, what=None, ):
        """
            Returns either the 'div' stats or the 'mid' stats based on the 'what' argument passed.

            Parameters
            ----------
            cols : list : The sequence object from which the datas will be taken from - self.cols.y
            nPlaces : int : The number of places that the stats must be rounded off to.
            what : str : The argument passed which decided which stat must be returned ("mid" or "div")
        """

        def fun(_, col):
            if what == "div":
                value = col.div()
            if what == "mid":
                value = col.mid()

            return col.rnd(value, nPlaces), col.txt

        return misc.kap(cols or self.cols.y, fun)

    def dist(self, row1, row2, cols=None, n=None, d=None):
        """
        Function for returning the distance between two rows.
        Returns a float which is the distance between row 1 and row 2
        """
        n, d = 0, 0
        cols = cols if cols else self.cols.x
        for col in cols:
            n = n + 1
            d = d + (col.dist(row1.cells[col.at], row2.cells[col.at]) ** the["p"])
        return (d / n) ** (1 / the["p"])

    def around(self, row1, rows=None, cols=None):
        """
        Sorting rows by the distance to row1
        """

        def func(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        return sorted(list(map(func, rows or self.rows)), key=itemgetter("dist"))

    def half(self, rows=None, cols=None, above=None):
        """
        Divides the data with 2 points
        """

        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        rows = rows or self.rows
        some = misc.many(rows, the['Sample'])
        A = above or any(some)
        B = self.around(A, some)[int(the['Far'] * len(rows)) // 1]['row']
        c = dist(A, B)
        left, right = [], []

        def project(row):
            return {'row': row, 'dist': cosine(dist(row, A), dist(row, B), c)}

        for n, tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('dist'))):
            if n < len(rows) // 2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A, B, mid, c

    def cluster(self, rows=None, cols=None, above=None):
        """
        Returns rows recursively halved
        """
        rows = rows or self.rows
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)}

        if len(rows) >= 2:
            left, right, node['A'], node['B'], node["mid"], _ = self.half(rows, cols, above)
            node['left'] = self.cluster(left, cols, node['A'])
            node['right'] = self.cluster(right, cols, node['B'])
        return node

    def better(self, row1, row2):
        """
        Checks and returns if row1 dominates
        """
        s1, s2 = 0, 0
        ys = self.cols.y
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def sway(self, rows=None, min=None, cols=None, above=None):
        """
        Returns the better half recursively
        """
        rows = rows or self.rows
        min = min or len(rows) ** the['min']
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)}
        if len(rows) > 2 * min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            if self.better(node['B'], node['A']):
                left, right, node['A'], node['B'] = right, left, node['B'], node['A']
            node['left'] = self.sway(left, min, cols, node['A'])
        return node

    def furthest(self, row1, rows=None, cols=None):
        t = self.around(row1, rows, cols)
        return t[len(t) - 1]

    def tree(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** the['min']
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)}
        if len(rows) >= 2 * min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            node['left'] = self.tree(left, min, cols, node['A'])
            node['right'] = self.tree(right, min, cols, node['B'])
        return node
