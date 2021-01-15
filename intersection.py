class Intersection:
    def __init__(self, ray_start, ray_end, wall_start, wall_end):
        self.p0_x = ray_start["x"]
        self.p0_y = ray_start["y"]
        self.p1_x = ray_end["x"]
        self.p1_y = ray_end["y"]
        self.p2_x = wall_start["x"]
        self.p2_y = wall_start["y"]
        self.p3_x = wall_end["x"]
        self.p3_y = wall_end["y"]

        self.a1 = self.p1_y - self.p0_y
        self.b1 = self.p0_x - self.p1_x
        self.c1 = (self.a1 * self.p0_x) + (self.b1 * self.p0_y)

        self.a2 = self.p3_y - self.p2_y
        self.b2 = self.p2_x - self.p3_x
        self.c2 = (self.a2 * self.p2_x) + (self.b2 * self.p2_y)

        self.denominator = (self.a1 * self.b2) - (self.a2 * self.b1)

    # Function determine whether ray intersects a wall segment
    # If so it returns the coordinate where it does
    def intersect_point(self):
        if self.denominator == 0:
            return None
        intersect_x = ((self.b2 * self.c1) - (self.b1 * self.c2)) / self.denominator
        intersect_y = ((self.a1 * self.c2) - (self.a2 * self.c1)) / self.denominator
        rx0 = (intersect_x - self.p0_x) / (self.p1_x - self.p0_x)
        ry0 = (intersect_y - self.p0_y) / (self.p1_y - self.p0_y)
        rx1 = (intersect_x - self.p2_x) / (self.p3_x - self.p2_x)
        ry1 = (intersect_y - self.p2_y) / (self.p3_y - self.p2_y)
        if ((0 <= rx0 <= 1) or (0 <= ry0 <= 1)) and ((0 <= rx1 <= 1) or (0 <= ry1 <= 1)):
            return {
                "x": intersect_x,
                "y": intersect_y
            }
        else:
            return None
