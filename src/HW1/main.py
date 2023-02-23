__author__ = "Group-6"
__version__ = "1.0.0"
__license__ = "MIT"


import sys, re, math
from test_all_HW1 import *
from misc import *
from config import *

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
    eg('the', 'show settings', test_theFun)
    eg('rand', 'generate, reset, regenerate same', test_randFun)
    eg('sym', 'check syms', test_symFun)
    eg('num', 'check nums', test_numFun)
    main()
