from modules import topLevel, UserAgent, motionData, Bezier, hCaptcha
import numpy as np
import random

class DV():
    def __init__(self):
        self.useragent = UserAgent.FakeUserAgent(browsers=["chrome"]).random
        self.pfmd = []

    def get_box_possibilities(self, points,thickness):
        return Bezier.Bez()._box(points=points,thickness=thickness)

    def create_curve_points(self, p1:list=[], p2:list=[], amount:int=20, box_points:list=[]):
        r = Bezier.Bez()._create(points=np.array([p1,random.choice(box_points),p2]), am_c=amount)
        return r

    def create_curves(self, points:list=[], am:int=10):
        prev_coord = [random.randint(0,200),random.randint(0,200)]
        box_points = self.get_box_possibilities(points=points,thickness=10)
        for x,y in points:
            pts = self.create_curve_points(p1=[x,y],p2=prev_coord, amount=am, box_points=box_points)
            for pt in pts:
                if pt != prev_coord: self.pfmd.append(pt)
            prev_coord = [x,y]
        return self.pfmd

    def complete_motion_data(self, curve_movement:list=[]):
        mot = motionData.Motion()
        data = mot.generate(data=curve_movement)
        """{
            "ts": self.ts,
            "te": self.te,
            "mm": self.mm,
            "md": self.md,
            "mu": self.mu
        }"""
        t = topLevel.topLevel()
        t.agentMod(self.useragent)
        t.dataMod(data)
        r = mot.create(topLevel=t._top, keyboard=False, HCAPLMAO=False)
        return r

    def rand_pts(self, pt_am:int=3):
        return np.random.rand(pt_am,2)*200
    
    def main(self, images, answers):
        hcap = hCaptcha.CapH(
            images=images,
            answers=answers
        )
        points = hcap._convert()
        self.create_curves(points=points,am=20)
        return str(self.complete_motion_data(self.pfmd)).replace("'",'"')

    def _bypassconv(self, points):
        self.create_curves(points=points,am=20)
        return str(self.complete_motion_data(self.pfmd)).replace("'",'"')

    def fun(self):
        motionData.Motion().f_hcap()

    def rev(self, mm):
        motionData.Motion().reverse(mm=mm)

    
"""    def _images(self, req):
        imgs = []
        for img in req["tasklist"]:
            imgs.append(req[img]["datapoint_uri"])

        return imgs
"""
        




print(DV()._bypassconv([
    [0,0],
    [100,100],
    [200,200]
]))
