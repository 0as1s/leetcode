from random import random
from typing import List
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
    def randPoint(self) -> List[float]:
        if self.r == 0:
            return [self.x, self.y]
        x = random() - 0.5 / 0.5
        x *= self.r
        y = random() - 0.5 / 0.5
        factor = math.sqrt(self.r*self.r - x*x) / self.r
        y *= factor * self.r

        if random() < 0.5:
            return [x, y]
        else:
            return [y, x]

    # Your Solution object will be instantiated and called as such:
    # obj = Solution(radius, x_center, y_center)
    # param_1 = obj.randPoint()


