__author__ = "NCSU CSC 591 Automated Software Engineering Group-6"
__version__ = "1.0.0"
__license__ = "MIT 2023"

import sys, re, math
from test_all_HW2 import *
from misc import *
from config import *


def main():
    """
        The main function takes in system arguments from the config.py file and runs all the examples. Runs all the tests
        and prints the status (pass/fail) of each test. Resets the random number seed every time it is run.

        Arguments
        ----------
         help str: A string variable in config.py containing the default global options.
         egs  dict: A dictionary containing the list of examples to be run as tests.
    """
    saved, fails = {}, 0

    for k, v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v

    if the['help']:
        print(help)
    else:
        for what, fun in egs.items():
            if the['go'] == 'all' or the['go'] == what:
                for k, v in saved.items():
                    the[k] = v
                Seed = the['seed']
                if not egs[what]():
                    fails += 1
                    print('❌ fail:', what)
                else:
                    print('✅ pass:', what)
    sys.exit(fails)
if __name__ == "__main__":
    eg("the", "testng the", test_the)
    eg("sym", "testing the sym class", test_sym)
    eg("num", "testing the num class", test_num)
    eg("rand", "testing Random function", test_rand)
    eg("csv", "testing CSV Function", test_csv)
    eg("data", "testing DATA for reading csv", test_data)
    eg("stats", "returning statistics from DATA", test_stats)
    main()
