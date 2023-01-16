"""
###                           __             /\ \__
###     ____    ___    _ __  /\_\    _____   \ \ ,_\
###    /',__\  /'___\ /\`'__\\/\ \  /\ '__`\  \ \ \/
###   /\__, `\/\ \__/ \ \ \/  \ \ \ \ \ \L\ \  \ \ \_
###   \/\____/\ \____\ \ \_\   \ \_\ \ \ ,__/   \ \__\
###    \/___/  \/____/  \/_/    \/_/  \ \ \/     \/__/
###                                    \ \_\
"""
import math

class obj:
    def __init__(self, s, t, new):
        self.id = 0

        def new(_, *args):
            self.id += 1
            i = {'a': s, 'id': id}
            i.update(t)
            t.new(i, *args)
            return i

        t = {}
        t.__index = t
        self.t = t
        self.new = new


# Summarize a stream of symbols
class SYM(obj):
    def __init__(self):
        super().__init__("SYM", {}, self.new)

    def new(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + (self.has[x] or 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for _, n in self.has.items():
            e += n / self.n * math.log(n / self.n, 2)
        return -e


# Summarizes a stream of numbers.
class NUM(obj):
    def __init__(self):
        super().__init__("NUM", {}, self.new)

    def new(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf

    def add(self, n):
        if n != "?":
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5