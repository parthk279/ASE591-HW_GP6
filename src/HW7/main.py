import sys, re, math
from test_all_HW7 import *
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
    eg("the", "testng the", test_the())
    eg("the", "testng the", eg())
    eg("num", "testing the num class", test_num())
    eg("rand", "testing Random function", test_rand())
    eg('nums', 'nums', test_num)
    eg('gauss', 'gauss', test_gauss)
    eg('five', 'five', test_five)
    eg('six', 'six', test_six)
    eg('tiles', 'tiles', test_tiles)
    eg('bootmu', 'bootmu', test_bootmu)
    eg('basic', 'basic', test_basic)
    eg('pre', 'pre', test_pre)
    eg('sk', 'sk', test_scKt)
    main()
