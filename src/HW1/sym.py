import math
import sys, random
class SYM:
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most=0,
        self.mode =None
    def add(self,x):
        if x != "?": 
             self.n = self.n + 1 
             if(self.has.get[x]!=None):
                self.has[x]=1+self.has[x]
             else:
                 self.has[x] = 1
             if self.has[x] > self.most:
                 self.most= self.has[x]
                 self.mode=x
             
    def mid(self):
       return self.mode
    def div(self,e):
        def fun(p):
            return p*math.log(p,2)
        e=0
        for n in self.has.items():
             e = e + fun(n/self.n)
        return -e