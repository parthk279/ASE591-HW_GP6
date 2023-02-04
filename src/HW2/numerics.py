Seed = 937162211


def rand(lo=0, hi=1):
    """
    Retruns the float value x between lo and hi
    """
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647


def rint(lo, hi):
    """
    Returns the rounded off digit of a random float value between lo and hi
    """
    return round(0.5 + rand(lo, hi))


def rnd(n, nPlaces=3):
    """
    Rounds off the digit to n number of places
    """
    return round(n * (10 ** nPlaces) + 0.5) / (10 ** nPlaces)
