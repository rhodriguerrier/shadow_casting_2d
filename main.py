from p5 import *
from rays import Rays
import random
from construct_walls import Wall

# Variables to be used throughout
wall_file = "wall_data.txt"
num_walls = 0
wall_coords = []
end_points = []
treasure = [150, 100]


# Function reads text file coordinates into 2d array
def load_walls(filename):
    walls = []
    with open(filename) as f:
        content = f.readlines()
    content = [x.rstrip('\n') for x in content]
    for points in content:
        x = [int(p) for p in points.split(",")]
        walls.append(x)
    return walls


def setup():
    size(500, 500)
    stroke(255, 255, 255)
    # Array containing all x and y coordinates of wall points
    construction_data = load_walls(wall_file)
    count = 0
    for wall_points in construction_data:
        temp_wall = Wall(wall_points[0], wall_points[1],
                         wall_points[2], wall_points[3])
        # Array to hold wall points
        wall_coords.append(temp_wall.get_wall())
        # Array to hold all end points for casting rays
        end_points.extend([temp_wall.get_first_end_point(),
                           temp_wall.get_second_end_point()])
        count += 1


def draw():
    background(0, 0, 0)
    ray_angles = []
    current_ray_start = {
        "x": mouse_x,
        "y": mouse_y
    }
    # Array that will hold all points to build light area
    shadow_points = []

    # Calculate angles of every end point and two either side
    for p in end_points:
        delta_x = p["x"] - current_ray_start["x"]
        delta_y = p["y"] - current_ray_start["y"]
        rads = math.atan2(delta_y, delta_x)
        ray_angles.extend([rads-0.00001, rads, rads+0.00001])

    # Sort angles so that light area is built in the correct order
    ray_angles.sort()

    for angle in ray_angles:
        current_ray = Rays(angle,
                           current_ray_start["x"],
                           current_ray_start["y"])
        count = 0
        # Loop through every wall for each ray to see which
        # walls intersect ray and which one is closest
        for wall in wall_coords:
            wall_start = {
                "x": wall["start_x"],
                "y": wall["start_y"]
            }
            wall_end = {
                "x": wall["end_x"],
                "y": wall["end_y"]
            }
            dist_to_wall = current_ray.intersect_adjust(current_ray_start, wall_start, wall_end)
            if count == 0:
                nearest_intersect = [dist_to_wall, current_ray.get_x2(), current_ray.get_y2()]
            elif dist_to_wall < nearest_intersect[0]:
                nearest_intersect = [dist_to_wall, current_ray.get_x2(), current_ray.get_y2()]
            count += 1
        shadow_points.append([nearest_intersect[1], nearest_intersect[2]])

    # Create polygon from end points to simulate light area
    fill(255)
    no_stroke()
    begin_shape()
    for points in shadow_points:
        vertex(points[0], points[1])
    end_shape()

    # This last section is a little game that moves a dot everytime the user's mouse lands on it
    # It's the same as the black background so appears missing when in shadow area
    point_to_treasure = math.sqrt((round(mouse_x, 0) - treasure[0])**2 + (round(mouse_y, 0) - treasure[1])**2)
    if point_to_treasure < 10:
        fill(0)
        no_stroke()
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        circle(x, y, 10)
        treasure[0] = x
        treasure[1] = y
    else:
        fill(0)
        no_stroke()
        circle(treasure[0], treasure[1], 10)


run()
