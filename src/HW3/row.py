class ROW:
    """
      Stores a single record for the row type object.
    """

    def __init__(self, t):
        """
          The constructor for the row class

          Parameters
          ----------
            t : list : The data to be read into and added to the ROW type object
        """
        self.cells = t
