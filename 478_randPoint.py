from random import random
from typing import List
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
    def randPoint(self) -> List[float]:
        rho = 2*random()*math.pi
        x = self.r*math.cos(rho)
        y = self.r*math.sin(rho)
        return [x,y]
