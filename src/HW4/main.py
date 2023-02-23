import sys, re, math
from test_all_HW4 import *
from misc import *
from config import *


def main():
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
                    print('❌ Fail:', what)
                else:
                    print('✅ Pass:', what)
    sys.exit(fails)


if __name__ == "__main__":
    eg("the", "testng the", test_theFun)
    eg("sym", "testing the sym class", test_symFun)
    eg("num", "testing the num class", test_numFun)
    eg("rand", "testing Random function", test_randFun)
    eg('repcols', 'checking repcols', test_repColsFun)
    eg('synonyms','checking repcols cluster', test_synonymsFun)
    eg('reprows','checking reprows', test_repRowsFun)
    eg('prototypes','checking reprows cluster', test_prototypesFun)
    eg('position','where\'s wally', test_positionFun)
    eg('every','the whole enchilada', test_everyFun)
    main()

