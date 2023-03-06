Seed = 937162211


def rand(lo=0, hi=1):
    """
        This is a rudimentary implementation of the random function from the random module in Python 3.x

        Parameters
        ----------
        lo : int : The lower bound of the range in which the random number must be generated from.
        hi : int : The higher bound of the range in which the random number must be generated from.

        Returns
        ---------
        float : A random number that lies between lo and hi.
    """
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647


def rint(lo, hi):
    """
        Implements the rand() function and returns the closest rounded off value of the float value generated
        between the two bounds lo and hi.

        Parameters
        ----------
        lo : int : The lower bound of the range in which the random number must be generated from.
        hi : int : The higher bound of the range in which the random number must be generated from.

        Returns
        ---------
        int : A random number that lies between lo and hi
    """
    return round(0.5 + rand(lo, hi))


def rnd(n, nPlaces=3):
    """
        Takes a float number and rounds it off to three decimal places.

        Parameters
        ----------
        n : float : The number that must be rounded off to by n places.
        nPlaces : int : The number of places that the number must be rounded off to.
    """
    return round(n * (10 ** nPlaces) + 0.5) / (10 ** nPlaces)