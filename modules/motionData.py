from datetime import datetime
import time
import random
class Motion():
    def __init__(self):
        self.kd = []
        self.timestamps = []
        self.av_timesamp = 0


        self.motiondata = {
            "mm": [],
            "topLevel": {}
        }

        self.keyboard = {'0': '48', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57', 'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70', 'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76', 'M': '77', 'N': '78', 'O': '79', 'P': '80', 'Q': '81', 'R': '82', 'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88', 'Y': '89', 'Z': '90'}

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

    def create(self, topLevel:dict={}, keyboard:bool=False, HCAPLMAO:bool=False, data:dict={}):

        self.motiondata["mm"] = data["mm"]
        self.motiondata["topLevel"] = topLevel
        
        self.motiondata["mm-mp"] = data["ts-mp"]
        
        self.motiondata["md"] = data["md"]
        self.motiondata["md-mp"] = round(((self.av_timesamp + random.randint(1,100)/100) * random.randint(4,6))*100)

        self.motiondata["mu"] = data["mu"]
        self.motiondata["mu-mp"] = round(((self.av_timesamp + random.randint(1,100)/100) * random.randint(4,6))*100)

        if keyboard:
            self.motiondata["kd"] = self.kb()

        if HCAPLMAO:
            self.motiondata["kd"] = self.f_hcap()

        self.motiondata["dct"] = int(time.time())
        self.motiondata["st"] = int(time.time())

        return self.motiondata