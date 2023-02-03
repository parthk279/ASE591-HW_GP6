import sys, re, math
from operator import itemgetter
from config import *
def misc(fun, iterable):
    """
    Maps the function over the iterable
    fun : Function that must be applied on each element of iterable
    iterable : iterable over which function must be mapped onto
    """
    u= []
    if iterable == None:
        return None
    elif fun == None:
        return u  
    else:
        return [fun(i) for i in iterable]

### NEED TO DO SORT ###
def eg(key, str, fun):
    egs[key] = fun
    global help
    help = help + '  -g '+ key + '\t' + str + '\n'
def keys(t: dict):
    """
    Returns the sorted list of dictionary keys
    t : dictionary
    """
    return sorted(t)
def fmt(*strings):
    """
    Emulating Print function
    """
    for string in strings:
        string = str(string)
        for s in string:
            sys.stdout.write(s)


def oo(t):
    """
    Emulating Print function and returning sorted value
    """
    print(t)
    if not isinstance(t, dict):
        return t
    else:
        return dict(sorted(t.items(), key=itemgetter(1)))


def settings(s):
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",s))

def coerce(s):
        if s == "true" or s == "True":
            return True
        elif s == "false" or s == "False":
            return False
        return s

    if s.isdigit():
        return int(s)
    elif "." in s and s.replace('.','').isdigit():
        return float(s)
    else:
        return s

def cli(options):
  args = sys.argv[1:]
  for k, v in options.items():
    v = str(v)
    for n, x in enumerate(args):
      if x == "-"+k[0] or  x == "--"+k:
        if v == "false":
            v = "true"
        elif v == "true":
            v = "false"
        else:
            v = arg[n + 1]
      options[k] = coerce(v)
    return options 


