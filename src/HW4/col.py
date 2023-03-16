from num import NUM
from sym import SYM


class COL:
    """
        The col class is a database for storing and dealing with NUM and SYM type objects
    """
    def __init__(self, names):
        """
         The constructor for COL class to hold column values.

         Data Members
         -----------
            names : the names of columns
            all  : data
            x  : x val
            y : y val
        """
        self.names = names
        self.all = []
        self.x = []
        self.y = []
        self.klass = None

        for col_name in names:
            if col_name[0].isupper():
                col = NUM(names.index(col_name), col_name)
            else:
                col = SYM(names.index(col_name), col_name)
            self.all.append(col)

            if not col_name[-1] == "X":
                if "+" in col_name or "!" in col_name:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if "!" in col_name:
                    self.klass = col

    def __str__(self):
        """
            The function for printing all the properties of the COL object

            Returns
            ------
            str : A formated string that contains the various attributes of the col object
        """
        return f"names is {self.names}, all is {self.all}, klass is {self.klass}, x is {self.x}, y is {self.y}"

    def add(self, row):
        """
            This function is sued to add a new ROW object for the columns with data.

            Parameters
            ----------
                row : ROW : The ROW object whose data will be added into the column

        """
        for t in [self.x, self.y]:
            for col in t:
                col.add(row.cells[col.at])
