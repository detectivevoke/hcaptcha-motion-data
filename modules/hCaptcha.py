import random

class CapH():
    def __init__(self, answers:dict={}):
        self.answers = answers
        self.images = self.answers.keys()
        self.boxes = {
            "0": self._betw([131,282],[177,310]),
            "1": self._betw([250,274],[313,318]),
            "2": self._betw([390,274],[438,324]),
            "3": self._betw([122,408],[187,456]),
            "4": self._betw([250,400],[314,451]),
            "5": self._betw([386,400],[448,466]),
            "6": self._betw([124,530],[188,584]),
            "7": self._betw([250,539],[313,588]),
            "8": self._betw([387,537],[446,579])
        }
        self.points = []

    def _betw(self, p1:list=[], p2:list=[]):
        points = []
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            for y in range(min(p1[1], p2[1]), max(p1[1],p2[1]) + 1):
                points.append([x, y])
        return points

    def _point(self, img_id:str="None"):
        return random.choice(self.boxes[str(self.images.index(img_id))])

    def _convert(self):
        for answer in self.answers:
            if self.answers[answer] == "true":
                self.points.append(self._point(img_id=answer))
        
        return self.points

