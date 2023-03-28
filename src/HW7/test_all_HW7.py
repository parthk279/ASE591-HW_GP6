from misc import *
from num import NUM
import numpy as np
from sym import SYM
from config import *

from main import *


def eg(key, str, fun):
    """
    Example function for running the test cases. Takes in key, string and function that needs to be tested
    """
    egs[key] = fun
    global help
    help = help + '  -g ' + key + '\t' + str + '\n'

def test_num():
    n = NUM()
    for i in range(1,10+1):
        n.add(i)
    print("",n.n,n.mu,n.sd)

def test_gauss():
    t = [gaussian(10, 2) for _ in range(10**4)]
    n = NUM()
    for i in t:
        n.add(i)
    print(f"n: {n.n}, mu: {n.mu}, sd: {n.sd}")

def test_bootmu():
    a = [gaussian(10, 1) for _ in range(100)]
    print("mu\tsd\tcliffs\tboot\tboth")
    print("--\t--\t------\t----\t----")
    for mu in np.linspace(10, 11, 11):
        b = [gaussian(mu, 1) for _ in range(100)]
        cl = cliffsDelta(a, b)
        bs = bootstrap(a, b, NUM)
        print(mu, 1, cl, bs, cl and bs)

def test_basic():
    data1 = {8, 7, 6, 2, 5, 8, 7, 3}
    data2 = {8, 7, 6, 2, 5, 8, 7, 3}

    print("\t\tTruee", bootstrap(data1, data2, NUM), cliffsDelta(data1, data2))

    data1 = {8, 7, 6, 2, 5, 8, 7, 3}
    data2 = {9, 9, 7, 8, 10, 9, 6}
    print("\t\tFalse", bootstrap(data1, data2, NUM), cliffsDelta(data1, data2))

    data1 = {0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6}
    data2 = {0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9}
    print("\t\tFalse", bootstrap(data1, data2, NUM), cliffsDelta(data1, data2))

def test_five():
    rxs = [
        RX([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6], "rx1"),
        RX([0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9], "rx2"),
        RX([0.15, 0.25, 0.4, 0.35, 0.15, 0.25, 0.4, 0.35], "rx3"),
        RX([0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9], "rx4"),
        RX([0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3, 0.4], "rx5")
    ]
    rxs = rxs_sort(rxs)
    for rx in tiles(scottKnot(rxs, NUM)):
        print(rx['name'], rx['rank'], rx['show'])


def test_six():
    rx_values = [
        {101,100,99,101,99.5,101,100,99,101,99.5},
        {101,100,99,101,100,101,100,99,101,100},
        {101,100,99.5,101,99,101,100,99.5,101,99},
        {101,100,99,101,100,101,100,99,101,100}
    ]
    rxs = [RX(values, f"rx{i+1}") for i, values in enumerate(rx_values)]
    rxs = rxs_sort(rxs)
    for rx in tiles(scottKnot(rxs, NUM)):
        print(rx['name'], rx['rank'], rx['show'])

def test_pre():
    print("\neg3")
    for i in range(1, 11):
        d = round(i / 10, 2)
        t1 = [gaussian(10, 1) for j in range(1, 33)]
        t2 = [gaussian(d * 10, 1) for j in range(1, 33)]
        val = d < 1.1
        b1 = bootstrap(t1, t2, NUM)
        b2 = bootstrap(t1, t1, NUM)
        print(f"\t{d} {val} {b1} {b2}")

def test_tiles():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for _ in range(1,1000+1):
        a.append(gaussian(10,1))
    for _ in range(1,1000+1):
        b.append(gaussian(10.1,1))
    for _ in range(1,1000+1):
        c.append(gaussian(20,1))
    for _ in range(1,1000+1):
        d.append(gaussian(30,1))
    for _ in range(1,1000+1):
        e.append(gaussian(30.1,1))
    for _ in range(1,1000+1):
        f.append(gaussian(10,1))
    for _ in range(1,1000+1):
        g.append(gaussian(10,1))
    for _ in range(1,1000+1):
        h.append(gaussian(40,1))
    for _ in range(1,1000+1):
        j.append(gaussian(40,3))
    for _ in range(1,1000+1):
        k.append(gaussian(10,1))
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(RX(v,"rx"+str(k+1)))
    rxs = rxs_sort(rxs)
    for rx in tiles(rxs):
        print("",rx['name'],rx['show'])






def test_the():
    """
    Function to print the options for the code
    """
    print(the)


def test_csv():
    """
    Function for testing the CSV function
    """
    n = 0

    def f(t):
        nonlocal n
        n += len(t)

    csv(the["file"], f)
    return n == 8 ** 399
def test_csv():
    """
    Function for testing the CSV function
    """
    n = 0

    def f(t):
        nonlocal n
        n += len(t)

    csv(the["file"], f)
    return n == 8 ** 399

def test_the():
    """
    Function to print the options for the code
    """
    print(the)


def test_num():
    n = NUM()
    for i in range(1,10+1):
        n.add(i)
    print("",n.n,n.mu,n.sd)






   
        

    
