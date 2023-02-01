import time
import random
import math
from itertools import islice


class Time():
    def __init__(self, rnge:int=20, xy:list=[]):
        self.current_timestamp = time.time()
        self.timestamps = []
        for i in range(rnge):
            self.timestamps.append(self.current_timestamp+i)
        self.xy = xy
        self.rnge = rnge
        self.split_xy = []
        self.ts = []
        self.te = []
        self.mm = []
        self.md = []
        self.kd = []
        self.mu = []
        self.avts = []
        self.av_timestamp = 0

    def _split(self):
        rand_n = [random.random() for i in range(self.rnge)]
        self.split_xy = [list(islice(iter(self.xy), elem))
                for elem in [math.floor(i * len(self.xy) / sum(rand_n)) for i in rand_n]]
        return True

    def av_ts(self):
        for i in self.avts:
            t = []
            idx = self.avts.index(i)
            for j in range(len(self.avts)):
                if(idx == j):
                    continue
                t.append(int(i/1000 - self.avts[j]/1000))
        self.av_timestamp = int(str(round(sum(t) / len(t))).replace("-",""))
        return True

    def _mm(self, ts, y, v):
        return int(ts + v + y * 900)

    def _setts(self):
        for set in self.split_xy:
            for x in set:
                self.mm.append([round(x[0]),round(x[1]), self._mm(self.timestamps[self.split_xy.index(set)], x[1], 20000)])
                self.avts.append(self._mm(self.timestamps[self.split_xy.index(set)], x[1], 20000))
                self.md.append([round(x[0]),round(x[1]), self._mm(self.timestamps[self.split_xy.index(set)], x[1], 20002)])
                self.mu.append([round(x[0]),round(x[1]), self._mm(self.timestamps[self.split_xy.index(set)], x[1], 20004)])
                self.te.append([0, round(x[0]), self._mm(self.timestamps[self.split_xy.index(set)], x[1], 19990)])
                self.ts.append([0, round(x[0]), self._mm(self.timestamps[self.split_xy.index(set)], x[1], 19990)])
        
        self.av_ts()

        return {
            "ts": self.ts,
            "te": self.te,
            "mm": self.mm,
            "md": self.md,
            "mu": self.mu,
            "ts-mp": self.av_timestamp
        }

    def main(self):
        self._split()
        return self._setts()
