import sys, re, math, yaml
from test_all import *
from misc import *
from test_all import test_eg
from config import *

def main():
  saved, fails={},0
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
              print('❌ Fail:', what)
          else:
              print('✅ Pass:', what)
  sys.exit(fails)


if __name__ == "__main__":
  eg("the", "testng the", test_the)
  eg("rand", "testing Random function", test_rand)
  eg("sym", "testing the sym class", test_sym)
  eg("num", "testing the num class", test_num)