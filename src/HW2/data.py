from misc import *
from row import ROW
from col import COL


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
            csv(src, self.add)
        else:
            for i in src:
                self.add(i)

    def add(self, t):
        """
            Function for adding a new ROW type object and appending the column headers of the DATA object

            Parameters
            ----------
            t : list : The data that needs to be appended as a new row or for updating the column headers.
        """
        if self.cols:
            if isinstance(t, list):
                t = ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COL(t)

    def clone(self):
        """
            Creates and Returns another data object that is a copy of the current DATA object.

            Returns
            -------
            data : DATA : A clone of the self DATA object
        """
        data = DATA(self.cols.names)
        for x in self.rows or []:
            data.add(x)
        return data

    def stats(self, cols=None, nPlaces=None, what=None,):
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

        return kap(cols or self.cols.y, fun)
