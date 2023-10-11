from A03_2_solution import Point, Polygon
import math


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
    except Exception as e:
        print(f"[EXPTN] Point(): {e}")
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
            print("[C-ERR] randomize()")
    except Exception as e:
        print(f"[EXPTN] randomize: {e}")
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
            print("[C-ERR] set_x/y & get_x/y")
    except Exception as e:
        print(f"[EXPTN] set/get x/y: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_length
        if d.get_length() == 2:
            print("[ OK  ] get_length()")
            score += 1
        else:
            print("[C-ERR] get_length()")
    except Exception as e:
        print(f"[EXPTN] get_length: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_distance
        if a.get_distance(d) == 2:
            print("[ OK  ] get_distance()")
            score += 1
        else:
            print(f"[C-ERR] get_distance(): {a.get_distance(d)} instead of 2")
    except Exception as e:
        print(f"[EXPTN] get_distance: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_quadrant
        if a.get_quadrant() == 3 and b.get_quadrant() == 4 and d.get_quadrant() == 0:
            print("[ OK  ] get_quadrant()")
            score += 1
        else:
            print(
                f"[C-ERR] get_quadrant(): {a.get_quadrant()}, {b.get_quadrant()}, {d.get_quadrant()} instead of 3, 4, 0")
    except Exception as e:
        print(f"[EXPTN] get_quadrant: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_angle(c)
        if round(b.get_angle(c), 1) == round(math.degrees(math.atan2(2 - (-3), 3 - 2)), 1):
            print(f"[ OK  ] get_angle(c)")
            score += 1
        else:
            print(
                f"[C-ERR] get_angle(c): {round(b.get_angle(c), 1)} instead of {round(math.degrees(math.atan2(2 - (-3), 3 - 2)), 1)}")
    except Exception as e:
        print(f"[EXPTN] get_angle(c): {e}")
    finally:
        num_tests += 1
    print("or")
    try:
        # Test get_angle, in case of misunderstanding in class (don't add to num_tests)
        # Test for negative angles as well
        if round(b.get_angle(), 1) == round(math.degrees(math.atan2(-3, 2)), 1) or round(b.get_angle(), 1) == round(math.degrees(math.atan2(-3, 2)), 1) + 360:
            print("[ OK  ] get_angle()")
            score += 1
        else:
            print(
                f"[C-ERR] get_angle(): {round(b.get_angle(), 1)} instead of {round(math.degrees(math.atan2(-3, 2)), 1)}")
    except Exception as e:
        print(f"[EXPTN] get_angle(): {e}")
    # finally:
    #     num_tests += 1

    point_score = round(score/num_tests * 100)
    print(f"POINT: {point_score}%")

    print("\n### POLYGON BASIC TESTING ###")
    score, num_tests = 0, 0

    try:
        poly = Polygon()
    except Exception as e:
        print(f"[EXPTN] Polygon(): {e}")
    else:
        print("[ OK  ] Polygon()")
        score += 1
    finally:
        num_tests += 1

    try:
        # Test add_point
        poly.add_point(Point(-2, -2))
        poly.add_point(Point(2, -3))
        poly.add_point(Point(3, 2))
        poly.add_point(Point(-2, 0))
        if len(poly.points) == 4:
            print("[ OK  ] add_point")
            score += 1
        else:
            print(f"[C-ERR] add_point: {len(poly.points)} instead of 4")
    except Exception as e:
        print(f"[EXPTN] add_point: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_num_points
        if poly.get_num_points() == 4:
            print("[ OK  ] get_num_points")
            score += 1
        else:
            print(
                f"[C-ERR] get_num_points: {poly.get_num_points()} instead of 4")
    except Exception as e:
        print(f"[EXPTN] get_num_points: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_circumference()
        if round(poly.get_circumference(), 1) == 16.6:
            print("[ OK  ] get_circumference")
            score += 1
        else:
            print(
                f"[C-ERR] get_circumference: {round(poly.get_circumference(), 1)} instead of 16.6")
    except Exception as e:
        print(f"[EXPTN] get_circumference: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_longest_side()
        if round(poly.get_longest_side(), 1) == 5.4:
            print("[ OK  ] get_longest_side")
            score += 1
        else:
            print(
                f"[C-ERR] get_longest_side: {round(poly.get_longest_side(), 1)} instead of 5.4")
    except Exception as e:
        print(f"[EXPTN] get_longest_side: {e}")
    finally:
        num_tests += 1

    try:
        # Test clear_points
        # TEST IN THE END!!!
        poly_no_unique_points = Polygon()
        poly_no_unique_points.add_point(Point(0, 1))
        poly_no_unique_points.add_point(Point(2, 3))
        poly_no_unique_points.add_point(Point(5, 3))
        poly_no_unique_points.clear_points()
        if len(poly_no_unique_points.points) == 0:
            print("[ OK  ] clear_points")
            score += 1
        else:
            print("[C-ERR] clear_points")
    except Exception as e:
        print(f"[EXPTN] clear_points: {e}")
    finally:
        num_tests += 1

    poly_basic_score = round(score/num_tests * 100)
    print(f"POLYGON BASIC: {poly_basic_score}%")

    print("\n### POLYGON ADVANCED TESTING ###")
    score, num_tests = 0, 0

    # Test-Polygon 2
    poly_no_unique_points = Polygon()
    poly_no_unique_points.add_point(Point(0, 1))
    poly_no_unique_points.add_point(Point(2, 3))
    poly_no_unique_points.add_point(Point(5, 3))
    poly_no_unique_points.add_point(Point(2, 3))

    # Test-Polygon 3, Area = 8.625
    poly3 = Polygon()
    poly3.add_point(Point(0, 0))
    poly3.add_point(Point(2, 0))
    poly3.add_point(Point(2.5, 2.5))
    poly3.add_point(Point(0, 3.5))
    poly3.add_point(Point(-1, 2))

    # Test-Polygon 4, complex, Area = 1.6, has 4 points
    poly4 = Polygon()
    poly4.add_point(Point(4.2, 0.2))
    poly4.add_point(Point(5.8, 1.8))
    poly4.add_point(Point(4, 2))
    poly4.add_point(Point(5.8, 0.2))

    try:
        # Test has_unique_points()
        if poly.has_unique_points() == True and poly_no_unique_points.has_unique_points() == False:
            print("[ OK  ] has_unique_points")
            score += 1
        else:
            print("[C-ERR] has_unique_points")
    except Exception as e:
        print(f"[EXPTN] has_unique_points: {e}")
    finally:
        num_tests += 1

    try:
        # Test get_area()
        if round(poly3.get_area(), 1) == 8.6:
            print("[ OK  ] get_area")
            score += 1
        else:
            print(
                f"[C-ERR] get_area: {round(poly3.get_area(), 1)} instead of 8.6")
    except Exception as e:
        print(f"[EXPTN] get_area: {e}")
    finally:
        num_tests += 1

    # try:
    #     # Test is_regular()
    #     if poly.is_regular() == True and poly3.is_regular() == False:
    #         print("[ OK  ] is_regular")
    #         score += 1
    #     else:
    #         print("[C-ERR] is_regular")
    # except Exception as e:
    #     print(f"[EXPTN] is_regular: {e}")
    # finally:
    #     num_tests += 1

    # Calculate if polygon advanced testing score is bigger than
    poly_adv_score = round(score/num_tests * 100)
    print(f"POLYGON ADVANCED: {poly_adv_score}%")

    # Print score summary
    print()
    print("### SCORE SUMMARY ###")
    print(f"POINT:       {point_score}%")
    print(f"POLYGON BAS: {poly_basic_score}%")
    print(f"POLYGON ADV: {poly_adv_score}%")

    print()


test()
