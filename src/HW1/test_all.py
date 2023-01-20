from misc import *
from num import NUM
from numerics import *
from sym import SYM
import yaml

with open("config.yml", "r") as config_file:
    cfg = yaml.safe_load(config_file)


def eg(key, str, fun):
  cfg.egs[key] = fun
  global help
  help = help + fmt("  -g  %s\t%s\n",key,str)

def test_rand():
    n1, n2 = NUM(), NUM()
    global Seed
    Seed = cfg["the"]['seed']
    for i in range(1,10**3+1):
        n1.add(rand(0,1))
    Seed = cfg["the"]['seed']
    for i in range(1,10**3+1):
        n2.add(rand(0,1))
    m1,m2 = rnd(n1.mid(),1), rnd(n2.mid(),1)
    return m1==m2 and .5 == rnd(m1,1)

def test_sym():
    sym = SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())

def test_num():
    num = NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())

def test_the():
  print(cfg["the"])

