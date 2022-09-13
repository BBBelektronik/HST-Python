from A03_2_solution import *

print("\n### POINT TESTING ###")
# Hier wird der Code getestet! z.B.

try:
    # Test Point
    a = Point(-2, -2)
    b = Point(2, -3)
    c = Point(0, 0)
    d = Point(-2, 0)
except Exception:
    print("[ERROR] Setting Point")

try:
    # Test randomize
    c.randomize(100)
    if 0 < c.x < 100 and 0 < c.y < 100:
        print("[ OK  ] randomize()")
    else:
        print("[ERROR] randomize()")
except Exception:
    print("[ERROR] randomize")


try:
    # Test set/get x/y
    c.set_x(3)
    c.set_y(2)
    if c.get_x() == 3 and c.get_y() == 2:
        print("[ OK  ] set_x/y & get_x/y")
    else:
        print("[ERROR] set_x/y & get_x/y")
except Exception:
    print("[ERROR] set/get x/y")


try:
    # Test get_length
    if d.get_length() == 2:
        print("[ OK  ] get_length()")
    else:
        print("[ERROR] get_length()")
except Exception:
    print("[ERROR] get_length")


try:
    # Test get_distance
    if a.get_distance(d) == 2:
        print("[ OK  ] get_distance()")
    else:
        print("[ERROR] get_distance()")
except Exception:
    print("[ERROR] get_distance")


try:
    # Test get_quadrant
    if a.get_quadrant() == 3 and b.get_quadrant() == 4 and c.get_quadrant() == 1:
        print("[ OK  ] get_quadrant()")
    else:
        print("[ERROR] get_quadrant()")
except Exception:
    print("[ERROR] get_quadrant")


try:
    # Test get_angle
    if round(b.get_angle(c), 1) == round(math.degrees(math.atan2(2 - (-3), 3 - 2)), 1):
        print("[ OK  ] get_angle")
    else:
        print("[ERROR] get_angle")
except Exception:
    print("[ERROR] get_angle")


print("\n### POLYGON TESTING ###")

try:
    reg = Polygon()
    reg.add_point(Point(-2, -2))
    reg.add_point(Point(2, -3))
    reg.add_point(Point(3, 2))
    reg.add_point(Point(-2, 0))
except Exception:
    print("[ERROR] Polygon()")

try:
    # Test add_point
    if len(reg.points) == 4:
        print("[ OK  ] add_point")
    else:
        print("[ERROR] add_point")
except Exception:
    print("[ERROR] add_point")


try:
    # Test get_num_points
    if len(reg.points) == reg.get_num_points():
        print("[ OK  ] get_num_points")
    else:
        print("[ERROR] get_num_points")
except Exception:
    print("[ERROR] get_num_points")


try:
    # Test get_circumference()
    if round(reg.get_circumference(), 1) == 16.6:
        print("[ OK  ] get_circumference")
    else:
        print("[ERROR] get_circumference")
except Exception:
    print("[ERROR] get_circumference")


try:
    # Test get_longest_side()
    if round(reg.get_longest_side(), 1) == 5.4:
        print("[ OK  ] get_longest_side")
    else:
        print("[ERROR] get_longest_side")
except Exception:
    print("[ERROR] get_longest_side")

try:
    # Test clear_points
    # TEST IN THE END!!!
    reg.clear_points()
    if len(reg.points) == 0:
        print("[ OK  ] clear_points")
    else:
        print("[ERROR] clear_points")
except Exception:
    print("[ERROR] clear_points")