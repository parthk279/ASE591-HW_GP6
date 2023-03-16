from misc import *
import misc
from row import ROW
from col import COL
from config import *
from numerics import *
import math
from pathlib import Path

from row import ROW
from misc import *
from operator import itemgetter


class DATA:
    """
        The DATA class is used to act as a container for the information in ROW type objects but is summarized in the
        form of COL type objects.
    """
    def __init__(self, src):
        """
            Constructor for creating a DATA type object

            Parameters
            ----------
            src : str : The path to the File whose data needs to be added into the DATA object
        """
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            misc.csv(src, self.add)
        else:
            for row in src:
                self.add(row)

    def add(self, t):
        """
            Function for adding a new ROW type object and appending the column headers of the DATA object

            Parameters
            ----------
            t : list : The data that needs to be appended as a new row or for updating the column headers.
        """
        if self.cols:
            t = ROW(t) if type(t) == list else t
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COL(t)

    def clone(self, init={}):
        """
            Creates and Returns another data object that is a copy of the current DATA object.

            Returns
            -------
            data : DATA : A clone of the self DATA object
        """
        data = DATA([self.cols.names])
        _ = list(map(data.add, init))
        return data

    def stats(self, cols=None, nPlaces=None, what=None):
        """
            Returns either the 'div' stats or the 'mid' stats based on the 'what' argument passed.

            Parameters
            ----------
            cols : list : The sequence object from which the datas will be taken from - self.cols.y
            nPlaces : int : The number of places that the stats must be rounded off to.
            what : str : The argument passed which decided which stat must be returned ("mid" or "div")
        """

        def fun(_, col):
            if what == 'div':
                val = col.div()
            else:
                val = col.mid()
            return col.rnd(val, nPlaces), col.txt

        return kap(cols or self.cols.y, fun)

    def dist(self, row1, row2, cols=None):
        """
            Function for returning the distance between two rows.

            Parameters
            ----------
            row1 : ROW : The first row from which distance must be calculated from
            row2 : ROW : The second row from which distance must be calculated from
            cols : COL : The Column that holds the location of the rows

            Returns
            -------
                float : The distance between row 1 and row 2
        """
        n, d = 0, 0
        for col in cols or self.cols.x:
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** the['p']
        return (d / n) ** (1 / the['p'])

    def around(self, row1, rows=None, cols=None):
        """
            Function for sorting  rows by the distance to row1

            Parameters
            ----------
            row1 : ROW : The ROW from which the distance is calculated from
            rows : list[ROW] : The list of rows which need to be sorted. Takes 'self.rows' if nothing is mentioned
            cols : COL : The COL object to manage rows
        """

        def function(row2):
            return {'row': row2, 'dist': self.dist(row1, row2, cols)}

        return sorted(list(map(function, rows or self.rows)), key=itemgetter('dist'))

    def half(self, rows=None, cols=None, above=None):
        """
            Divides the data with 2 points

            Parameters
            ----------
            rows : list[ROW] : The list of rows that need to be halved
            cols : COL : COL object to store the ROW data
            above : ROW : The row above which it must be halved.
        """

        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        rows = rows or self.rows
        A = above or any(rows)
        B = self.furthest(A, rows)['row']
        c = dist(A, B)
        left, right = [], []

        def project(row):
            x, y = cosine(dist(row, A), dist(row, B), c)
            try:
                row.x = row.x
                row.y = row.y
            except:
                row.x = x
                row.y = y
            return {'row': row, 'x': x, 'y': y}

        for n, tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('x'))):
            if n < len(rows) // 2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A, B, mid, c

    def cluster(self, rows=None,  cols=None, above=None):
        """
            Returns rows recursively halved

            Parameters
            ---------
            rows : list[ROW] : The list of ROW objects for which the better half must be returned
            min : int : The minimum number of clusters
            cols : COL : The COL object to hold ROW values
            above : ROW : The row around which clustering is formed
        """
        rows = rows or self.rows
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)}
        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'] = self.half(rows, cols, above)
            node['left'] = self.cluster(left, cols, node['A'])
            node['right'] = self.cluster(right, cols, node['B'])
        return node

    def better(self, row1, row2):
        """
            Checks if the ROW1 will dominate row2

            Parameters
            ----------
            row1 : ROW : The first row to check if it dominates the second
            row2 : ROW : The second row which is used as benchmark for checking if dominated by first row

            Returns
            -------
            bool : Checks if s1/len(ys) < s2/len(ys). This way we will know if row1 dominates row2 or not
        """
        s1, s2, ys = 0, 0, self.cols.y
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def sway(self, rows=None, min=None, cols=None, above=None):
        """
            Returns the better half recursively

            Parameters
            ---------
            rows : list[ROW] : The list of ROW objects for which the better half must be returned
            min : int : The minimum number of clusters
            cols : COL : The COL object to hold ROW values
            above : ROW : The chose row around which clustering is formed
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
        """
            This sorts other rows based on the distance to row
        """
        t = self.around(row1, rows, cols)
        return t[len(t) - 1]
