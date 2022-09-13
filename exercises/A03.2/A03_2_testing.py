from A03_2_solution import *


def test():
    print("\n### POINT TESTING ###")
    # Hier wird der Code getestet! z.B.
    score, num_tests = 0.0, 0.0
    try:
        # Test Point
        a = Point(-2, -2)
        b = Point(2, -3)
        c = Point(0, 0)
        d = Point(-2, 0)
    except Exception:
        print("[ERROR] Point()")
    else:
        print("[ OK  ] Point()")
        score += 1
    finally:
        num_tests += 1

    try:
        # Test randomize
        max = 10000
        c.randomize(max)
        if -max <= c.x <= max and -max <= c.y <= max:
            print("[ OK  ] randomize()")
            score += 1
        else:
            print("[ERROR] randomize()")
    except Exception:
        print("[ERROR] randomize")
    finally:
        num_tests += 1

    try:
        # Test set/get x/y
        c.set_x(3)
        c.set_y(2)
        if c.get_x() == 3 and c.get_y() == 2:
            print("[ OK  ] set_x/y & get_x/y")
            score += 1
        else:
            print("[ERROR] set_x/y & get_x/y")
    except Exception:
        print("[ERROR] set/get x/y")
    finally:
        num_tests += 1

    try:
        # Test get_length
        if d.get_length() == 2:
            print("[ OK  ] get_length()")
            score += 1
        else:
            print("[ERROR] get_length()")
    except Exception:
        print("[ERROR] get_length")
    finally:
        num_tests += 1

    try:
        # Test get_distance
        if a.get_distance(d) == 2:
            print("[ OK  ] get_distance()")
            score += 1
        else:
            print("[ERROR] get_distance()")
    except Exception:
        print("[ERROR] get_distance")
    finally:
        num_tests += 1

    try:
        # Test get_quadrant
        if a.get_quadrant() == 3 and b.get_quadrant() == 4 and c.get_quadrant() == 1:
            print("[ OK  ] get_quadrant()")
            score += 1
        else:
            print("[ERROR] get_quadrant()")
    except Exception:
        print("[ERROR] get_quadrant")
    finally:
        num_tests += 1

    try:
        # Test get_angle
        if round(b.get_angle(c), 1) == round(math.degrees(math.atan2(2 - (-3), 3 - 2)), 1):
            print("[ OK  ] get_angle")
            score += 1
        else:
            print("[ERROR] get_angle")
    except Exception:
        print("[ERROR] get_angle")
    finally:
        num_tests += 1

    print(f"POINT: {round(score/num_tests * 100)}%")

    print("\n### POLYGON BASIC TESTING ###")
    score, num_tests = 0, 0

    try:
        poly = Polygon()
        poly.add_point(Point(-2, -2))
        poly.add_point(Point(2, -3))
        poly.add_point(Point(3, 2))
        poly.add_point(Point(-2, 0))
    except Exception:
        print("[ERROR] Polygon()")
    else:
        print("[ OK  ] Polygon()")
        score += 1
    finally:
        num_tests += 1

    try:
        # Test add_point
        if len(poly.points) == 4:
            print("[ OK  ] add_point")
            score += 1
        else:
            print("[ERROR] add_point")
    except Exception:
        print("[ERROR] add_point")
    finally:
        num_tests += 1

    try:
        # Test get_num_points
        if len(poly.points) == poly.get_num_points():
            print("[ OK  ] get_num_points")
            score += 1
        else:
            print("[ERROR] get_num_points")
    except Exception:
        print("[ERROR] get_num_points")
    finally:
        num_tests += 1

    try:
        # Test get_circumference()
        if round(poly.get_circumference(), 1) == 16.6:
            print("[ OK  ] get_circumference")
            score += 1
        else:
            print("[ERROR] get_circumference")
    except Exception:
        print("[ERROR] get_circumference")
    finally:
        num_tests += 1

    try:
        # Test get_longest_side()
        if round(poly.get_longest_side(), 1) == 5.4:
            print("[ OK  ] get_longest_side")
            score += 1
        else:
            print("[ERROR] get_longest_side")
    except Exception:
        print("[ERROR] get_longest_side")
    finally:
        num_tests += 1

    try:
        # Test clear_points
        # TEST IN THE END!!!
        poly2 = Polygon()
        poly2.add_point(Point(0, 1))
        poly2.add_point(Point(2, 3))
        poly2.add_point(Point(5, 3))
        poly2.clear_points()
        if len(poly2.points) == 0:
            print("[ OK  ] clear_points")
            score += 1
        else:
            print("[ERROR] clear_points")
    except Exception:
        print("[ERROR] clear_points")
    finally:
        num_tests += 1

    print(f"POLYGON: {round(score/num_tests * 100)}%")

    print("\n### POLYGON ADVANCED TESTING ###")
    score, num_tests = 0, 0

    # Test-Polygon 2
    poly2 = Polygon()
    poly2.add_point(Point(0, 1))
    poly2.add_point(Point(2, 3))
    poly2.add_point(Point(5, 3))
    poly2.add_point(Point(2, 3))

    # Test-Polygon 3
    poly3 = Polygon()
    poly3.add_point(Point(0, 0))
    poly3.add_point(Point(2, 0))
    poly3.add_point(Point(3, 3))
    poly3.add_point(Point(1, 1))
    poly3.add_point(Point(0, 3))

    try:
        # Test has_unique_points()
        if poly.has_unique_points() == True and poly2.has_unique_points() == False:
            print("[ OK  ] has_unique_points")
            score += 1
        else:
            print("[ERROR] has_unique_points")
    except Exception:
        print("[ERROR] has_unique_points")
    finally:
        num_tests += 1

    # try:
    #     # Test get_area()
    #     if round(poly.get_area(), 1) == 15.5:
    #         print("[ OK  ] get_area")
    #         score += 1
    #     else:
    #         print("[ERROR] get_area")
    # except Exception:
    #     print("[ERROR] get_area")
    # finally:
    #     num_tests += 1

    # try:
    #     # Test is_regular()
    #     if poly.is_regular() == True and poly3.is_regular() == False:
    #         print("[ OK  ] is_regular")
    #         score += 1
    #     else:
    #         print("[ERROR] is_regular")
    # except Exception:
    #     print("[ERROR] is_regular")
    # finally:
    #     num_tests += 1


test()
