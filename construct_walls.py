# Returns wall coordinates in needed formats
# for endpoints and walls
class Wall:
    def __init__(self, start_x, start_y,
                 end_x, end_y):
        self.x_1 = start_x
        self.y_1 = start_y
        self.x_2 = end_x
        self.y_2 = end_y

    def get_wall(self):
        return {
            "start_x": self.x_1,
            "start_y": self.y_1,
            "end_x": self.x_2,
            "end_y": self.y_2
        }

    def get_first_end_point(self):
        return {
            "x": self.x_1,
            "y": self.y_1
        }

    def get_second_end_point(self):
        return {
            "x": self.x_2,
            "y": self.y_2
        }
