import math
from intersection import Intersection


class Rays:
    def __init__(self, rads, current_x,
                 current_y):
        self.rads = rads
        self.x2 = current_x + (1000 * math.cos(self.rads))
        self.y2 = current_y + (1000 * math.sin(self.rads))
        self.ray_end = {
            "x": self.x2,
            "y": self.y2
        }

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    # Function takes ray and wall coordinates to determine whether the
    # end point needs to change if intersection occurs
    def intersect_adjust(self, ray_start, wall_start, wall_end):
        intersect_obj = Intersection(ray_start, self.ray_end, wall_start, wall_end)
        adjustment = intersect_obj.intersect_point()
        if adjustment is not None:
            self.x2 = adjustment["x"]
            self.y2 = adjustment["y"]
        dist = absolute_distance(ray_start["x"], ray_start["y"], self.x2, self.y2)
        return dist


# Function find distance from two points so that the closest
# intersection point can be found
def absolute_distance(start_x, start_y, end_x, end_y):
    a_squared = abs(end_x - start_x) ** 2
    b_squared = abs(end_y - start_y) ** 2
    return math.sqrt(a_squared + b_squared)