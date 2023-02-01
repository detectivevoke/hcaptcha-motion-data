from datetime import datetime
import time
import random
class Motion():
    def __init__(self):
        self.ts = []
        self.te = []
        self.mm = []
        self.md = []
        self.kd = []
        self.mu = []
        self.timestamps = []
        self.av_timesamp = 0


        self.motiondata = {
            "mm": [],
            "topLevel": {}
        }

        self.keyboard = {'0': '48', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57', 'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70', 'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76', 'M': '77', 'N': '78', 'O': '79', 'P': '80', 'Q': '81', 'R': '82', 'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88', 'Y': '89', 'Z': '90'}

    def timest(self, y:int=0 ,n:int=20000):
        return int(int(time.time()) + n + y * 900)

    def generate(self, data:list=[]):
        for x, i in data:
            ts = self.timest(y=i, n=19900)
            self.ts.append(
                [[0, x], ts] # 19900 
            )
            
            ts = self.timest(y=i, n=19990)
            self.te.append(
                [[0,x], self.timest(y=i, n=19990)] # 19990 
            )

            ts = self.timest(y=i)
            self.timestamps.append(ts)
            self.mm.append(
                [round(x), round(i) ,self.timest(y=i, n=20000)]
            )

            ts = self.timest(y=i, n=20002)
            self.md.append(
                [round(x), round(i) ,self.timest(y=i, n=20002)] # 20002 
            )

            ts = self.timest(y=i, n=20004)
            self.mu.append(
                [round(x), round(i) , self.timest(y=i, n=20004)] # 20004 
            )
        
        self.av_timesamp = self.av_ts()

        return {
            "ts": self.ts,
            "te": self.te,
            "mm": self.mm,
            "md": self.md,
            "mu": self.mu,
            "ts-mp": self.av_timesamp
        }

    def f_hcap(self):
        x = "FUCKHCAPTCHALMFAO"
        for l in x:
            key = int(self.keyboard[l.upper()])
            timestamp = int(int(time.time()) + 20000 + key * 900)
            self.kd.append([key, timestamp])

        return self.kd

    def kb(self):
        for i in range(random.randint(3,10)):
            key_s = int(self.keyboard[random.choice(list(self.keyboard.keys()))])
            timestamp = int(int(time.time()) + 20000 + key_s * 900)
            self.kd.append([key_s, timestamp])

        return self.kd

    def av_ts(self):
        for i in self.timestamps:
            t = []
            idx = self.timestamps.index(i)
            for j in range(len(self.timestamps)):
                if(idx == j):
                    continue
                t.append(int(i/1000 - self.timestamps[j]/1000))
        return sum(t) / len(t)

    def reverse(self, mm:list=[]):
        for x,y,ts in mm:
            timestamp = ((ts-y*900)- 20000)
            print(datetime.fromtimestamp(timestamp/1000))

    def create(self, topLevel:dict={}, keyboard:bool=False, HCAPLMAO:bool=False):

        

        self.motiondata["mm"] = self.mm
        self.motiondata["topLevel"] = topLevel
        
        self.motiondata["mm-mp"] = self.av_timesamp/100
        
        self.motiondata["md"] = self.md
        self.motiondata["md-mp"] = (self.av_timesamp + random.randint(1,100)/100) * random.randint(4,6) 

        self.motiondata["mu"] = self.mu
        self.motiondata["mu-mp"] = (self.av_timesamp + random.randint(1,100)/100) * random.randint(4,6)

        if keyboard:
            self.motiondata["kd"] = self.kb()

        if HCAPLMAO:
            self.motiondata["kd"] = self.f_hcap()

        self.motiondata["dct"] = int(time.time())
        self.motiondata["st"] = int(time.time())

        return self.motiondata