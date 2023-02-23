from misc import *
from num import NUM
from sym import SYM
from config import *
from main import *



def test_randFun():
    n1, n2 = NUM(), NUM()
    global Seed
    Seed = the['seed']
    for i in range(1,10**3+1):
        n1.add(rand(0,1))
    Seed = the['seed']
    for i in range(1,10**3+1):
        n2.add(rand(0,1))
    m1,m2 = rnd(n1.mid(),1), rnd(n2.mid(),1)
    return m1==m2 and .5 == rnd(m1,1)

def test_symFun():
    sym = SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())

def test_numFun():
    num = NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())

def test_theFun():
  print(str(the))

