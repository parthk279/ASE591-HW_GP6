import sys, re, math, copy, json, random

from config import *
from operator import itemgetter
import os


def csv(fileName, fun):
    """
    Function for reading the csv file and applying a function over the text in csv file
    """

    if os.path.exists(fileName) and fileName.endswith(".csv"):
        with open(fileName, "r", encoding="utf-8") as file:
            for _, row in enumerate(file):
                r = list(map(coerce, row.strip().split(",")))
                fun(r)
    else:
        print("File does not exist at : ", fileName)
        return 0


def misc(fun, iterable):
    """
    Maps the function over the iterable
    fun : Function that must be applied on each element of iterable
    iterable : iterable over which function must be mapped onto
    """
    u = []
    if iterable is None:
        return None
    elif fun is None:
        return u
    else:
        return [fun(i) for i in iterable]


def eg(key, str, fun):
    """
    Function for running the example test cases in test files and main.py
    """
    egs[key] = fun
    global help
    help = help + '  -g ' + key + '\t' + str + '\n'


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
    """
    Using REGEX to read the settings
    """
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))

def dofile(sFile):
    file = open(sFile, 'r', encoding='utf-8')
    text  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))


def coerce(s):
    """
    Reading the values in s and reformatting it for test use
    """

    def fun(s1):
        if s1 == "true" or s1 == "True":
            return True
        elif s1 == "false" or s1 == "False":
            return False
        return s1

    if s.isdigit():
        return int(s)
    elif "." in s and s.replace(".", "").isdigit():
        return float(s)
    else:
        return fun(s.strip())


def cli(options):
    """
    Function for displaying and for printing the command line interface options.
    """
    arg = sys.argv[1:]
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(arg):
            if x == "-" + k[0] or x == "--" + k:
                if v == "false":
                    v = "true"
                elif v == "true":
                    v = "false"
                else:
                    v = arg[n + 1]
            options[k] = coerce(v)

        return options


def kap(iterable, fun):
    """
    Applies a function over a iterable and returns the result as key value pair with key as index
    and value as result of the function
    """
    result = {}
    for i in iterable:
        index = iterable.index(i)
        i, index = fun(index, i)
        result[index or len(result)] = i
    return result

def dkap(t, fun):
    u = {}
    for k,v in t.items():
        v, k = fun(k,v) 
        u[k or len(u)] = v
    return u

def push(t, x):
    t.append(x)
    return x




def many(iterable, n):
    """
    Returns a few items from an iterable
    """
    u = []
    for _ in range(1, n + 1):
        u.append(any(iterable))
    return u


def show(node, what, cols, n_places, lvl=0):
    """
    Prints the tree
    """
    if node:
        print('| ' * lvl + str(len(node['data'].rows)) + '  ', end='')
        if not node.get('left') or lvl == 0:
            print(node['data'].stats(node['data'].cols.y, n_places, "mid"))
        else:
            print('')
        show(node.get('left'), what, cols, n_places, lvl + 1)
        show(node.get('right'), what, cols, n_places, lvl + 1)

def deepcopy(t):
    return copy.deepcopy(t)

def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i]={}
        for j in range(1, n+1):
            g[i][j]=' '
    maxy = 0
    print('')
    for r,row in enumerate(data.rows):
        c = chr(97+r).upper()
        print(c, row.cells[-1])
        x,y= row.x*n//1, row.y*n//1
        maxy = int(max(maxy,y+1))
        g[y+1][x+1] = c
    print('')
    for y in range(1,maxy+1):
        print(' '.join(g[y].values()))

def showTree(node, what, cols, nPlaces, lvl = 0):
  if node:
    print('|.. ' * lvl + '[' + str(len(node['data'].rows)) + ']' + '  ', end = '')
    if not node.get('left') or lvl==0:
        print(node['data'].stats("mid",node['data'].cols.y,nPlaces))
    else:
        print('')
    showTree(node.get('left'), what,cols, nPlaces, lvl+1)
    showTree(node.get('right'), what,cols,nPlaces, lvl+1)



   
def prune(rule, maxSize):
    n=0
    for txt,ranges in rule.items():
        n = n+1
        if len(ranges) == maxSize[txt]:
            n=n+1
            rule[txt] = None
    if n > 0:
        return rule



def extend(range,n,s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])
    range['y'].add(s)

def itself(x):
    return x

def value(has,nB = None, nR = None, sGoal = None):
    sGoal,nB,nR = sGoal or True, nB or 1, nR or 1
    b,r = 0,0
    for x,n in has.items():
        if x==sGoal:
            b = b + n
        else:
            r = r + n
    b,r = b/(nB+1/float("inf")), r/(nR+1/float("inf"))
    return b**2/(b+r)


def merge2(col1,col2):
  new = merge(col1,col2)
  if new.div() <= (col1.div()*col1.n + col2.div()*col2.n)/new.n:
    return new

def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1,len(t)):
            t[j]['lo'] = t[j-1]['hi']
        t[0]['lo']  = float("-inf")
        t[len(t)-1]['hi'] =  float("inf")
        return t

    ranges1,j = [],0
    while j <= len(ranges0)-1:
        left = ranges0[j]
        right = None if j == len(ranges0)-1 else ranges0[j+1]
        if right:
            y = merge2(left['y'], right['y'])
            if y:
                j = j+1
                left['hi'], left['y'] = right['hi'], y
        ranges1.append(left)
        j = j+1
    return noGaps(ranges0) if len(ranges0)==len(ranges1) else mergeAny(ranges1)


def gaussian(mu, sd):
    mu, sd = mu or 0, sd or 1
    sq, pi, log, cos, r = math.sqrt, math.pi, math.log, math.cos, random.random
    return mu + sd * sq(-2 * log(r())) * cos(2 * pi * r())

def cliffsDelta(ns1,ns2):
    if len(ns1) > 128:
        ns1 = samples(ns1,128)
    if len(ns2) > 128:
        ns2 = samples(ns2,128)
    n,gt,lt = 0,0,0
    for x in ns1:
        for y in ns2:
            n = n + 1
            if x > y:
                gt = gt + 1
            if x < y:
                lt = lt + 1
    return abs(lt - gt)/n <= the['cliff']
def samples(t, n=None):
    p = {}
    for i in range(1, (n or len(t)) + 1):
        p[i] = t[random.randint(0, len(t) - 1)]
    return p
def delta(i, other):
  e, y, y1= 1E-32, i, other
  return (abs(y.mu - y1.mu) / ((e + y.sd**2/y.n + y1.sd**2/y1.n)**.5))

def bootstrap(y0,z0, NUM):
    x, y, z, yhat, zhat = NUM(), NUM(), NUM(), [], []
    for y1 in y0:
        x.add(y1)
        y.add(y1)
    for z1 in z0:
        x.add(z1)
        z.add(z1)
    xmu, ymu, zmu = x.mu, y.mu, z.mu
    for y1 in y0:
        yhat.append(y1 - ymu + xmu)
    for z1 in z0:
       zhat.append(z1 - zmu + xmu)
    tobs = delta(y,z)
    n = 0
    for _ in range(1,the['bootstrap']+1):
        i = NUM()
        other = NUM()
        for y in samples(yhat).values():
            i.add(y)
        for z in samples(zhat).values():
            other.add(z)
        if delta(i, other) > tobs:
            n = n + 1
    return n / the['bootstrap'] >= the['conf']

def RX(t,s): 
    t = sorted(t)
    return {'name' : s or "", 'rank':0, 'n':len(t), 'show':"", 'has':t}

def div(t):
  t= t['has'] if t['has'] else t
  return (t[ len(t)*9//10 ] - t[ len(t)*1//10 ])/2.56

def mid(t):
  t= t['has'] if t['has'] else t
  n = (len(t)-1)//2
  return (t[n] +t[n+1])/2 if len(t)%2==0 else t[n+1]

def merge(rx1,rx2):
    rx3 = RX([], rx1['name'])
    rx3['has'] = rx1['has'] + rx2['has']
    rx3['has'] = sorted(rx3['has'])
    rx3['n'] = len(rx3['has'])
    return rx3

def rxs_sort(rxs):
    for i,x in enumerate(rxs):
     for j,y in enumerate(rxs):
         if mid(x) < mid(y):
             rxs[j],rxs[i]=rxs[i],rxs[j]
    return rxs

def scottKnot(rxs, NUM):
  def merges(i,j):
    out = RX([],rxs[i]['name'])
    for k in range(i, j+1):
        out = merge(out, rxs[j])
    return out
  
  def same(lo,cut,hi):
    l= merges(lo,cut)
    r= merges(cut+1,hi)
    return cliffsDelta(l['has'], r['has']) and bootstrap(l['has'], r['has'], NUM)
  
  def recurse(lo,hi,rank):
    b4 = merges(lo,hi)
    best = 0
    cut = None
    for j in range(lo,hi+1):
      if j < hi:
        l   = merges(lo,  j)
        r   = merges(j+1, hi)
        now = (l['n']*(mid(l) - mid(b4))**2 + r['n']*(mid(r) - mid(b4))**2) / (l['n'] + r['n'])
        if now > best:
          if abs(mid(l) - mid(r)) >= cohen:
            cut, best = j, now
    if cut != None and not same(lo,cut,hi):
      rank = recurse(lo,    cut, rank) + 1
      rank = recurse(cut+1, hi,  rank) 
    else:
      for i in range(lo,hi+1):
        rxs[i]['rank'] = rank
    return rank
  rxs = rxs_sort(rxs)
  cohen = div(merges(0,len(rxs)-1)) * the['cohen']
  recurse(0, len(rxs)-1, 1)
  return rxs
