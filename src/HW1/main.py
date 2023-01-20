import sys, re, math, yaml
from test_all import *
from misc import *
from test_all import test_eg
with open("config.yml", "r") as config_file:
    cfg = yaml.safe_load(config_file)

def main():
  saved, fails={},0
  for k,v in cli(settings(help)).items():
      cfg["the"][k] = v
      saved[k] = v
  if cfg["the"]['help'] == True:
      print(help)
  else:
    for what, fun in cfg.egs.items():
        if cfg["the"]['go'] == 'all' or cfg["the"]['go'] == what:
          for k,v in saved.items():
              cfg["the"][k] = v
          Seed = cfg["the"]['seed']
          if cfg["egs"][what]() == False:
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