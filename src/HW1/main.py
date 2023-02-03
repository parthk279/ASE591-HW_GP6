__author__ = "Group-6"
__version__ = "1.0.0"
__license__ = "MIT"


import sys, re, math
from test_all import *
from misc import *
from config import *
help = """
script.py : an example script with help text and a test suite
(c)2023
USAGE:   script.py  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
"""
def main():
    saved,fails={},0
    for k,v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v
    if the['help'] == True:
        print(help)
    else:
        for what, fun in egs.items():
            if the['go'] == 'all' or the['go'] == what:
                for k,v in saved.items():
                    the[k] = v
                Seed = the['seed']
                if egs[what]() == False:
                    fails += 1
                    print('❌ fail:', what)
                else:
                    print('✅ pass:', what)
    sys.exit(fails)

if __name__ == '__main__':
    eg('the', 'show settings', test_the)
    eg('rand', 'generate, reset, regenerate same', test_rand)
    eg('sym', 'check syms', test_sym)
    eg('num', 'check nums', test_num)
    main()
