import math
import random
import time


class Point:
    def __init__(self, x=0, y=0):
        # 1. Überprüft, ob x und y numerisch (also int oder float) sind.
        # 2. Speichert die Argumente x und y als öffentliche Attribute ab.
        self.x = x if isinstance(x, (int, float)) else 0
        self.y = y if isinstance(y, (int, float)) else 0

    def get_x(self):
        # Gibt die x-Koordinate des Punktes zurück
        return self.x

    def get_y(self):
        # Gibt die y-Koordinate des Punktes zurück
        return self.y

    def get_xy(self):
        # Returns point as tuple
        return (self.x, self.y)

    def set_x(self, x):
        # 1. Überprüft, ob x numerisch ist.
        # 2. Falls ja: Speichert die x-Koordinate
        if isinstance(x, (int, float)):
            self.x = x
        pass

    def set_y(self, y):
        # 1. Überprüft, ob y numerisch ist.
        # 2. Falls ja: Speichert die y-Koordinate
        if isinstance(y, (int, float)):
            self.y = y
        pass

    def get_length(self):
        # Gibt die Distanz des Punktes vom Nullpunkt zurück (die "Länge" eines Punktes).
        # Tipp 1: Pythagoras
        # Tipp 2: Die Methode math.sqrt() von der Math-Library (import math) könnte hilfreich sein.
        return math.sqrt(self.x ** 2 + self.y ** 2)
        pass

    def get_quadrant(self):
        # Gibt als Integer zurück, in welchem Quadranten des Koordinatensystems sich der Punkt befindet.
        # Gibt 0 zurück, wenn der Punkt sich genau auf einer Achse befindet.
        if self.x > 0:
            if self.y > 0:
                return 1
            elif self.y < 0:
                return 4
        elif self.x < 0:
            if self.y > 0:
                return 2
            elif self.y < 0:
                return 3
        pass

    def randomize(self, max):
        # 1. Überprüft, ob 'max' ein numerischer Wert ist (int oder float)
        # 2. Falls ja: Generiert zufällige Werte für x und y (bis max) und speichert diese ab.
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # Tipp: Von random.randint(von, bis) bekommen Sie einen zufälligen Integer zw. 'von' und 'bis'
        if isinstance(max, (int, float)):
            self.x = random.randint(0, max)
            self.y = random.randint(0, max)
        else:
            raise ValueError
        pass

    def get_distance(self, to_point):
        # 1. Prüft, ob to_point vom Typ Point ist
        # 2. Falls ja: Berechnet die Distanz zwischen sich selber und einem anderen Punkt und gibt diese zurück.
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # Tipp: Die Methode math.sqrt() von der Math-Library (import math) könnte hilfreich sein.
        if isinstance(to_point, Point):
            dx = self.x - to_point.x
            dy = self.y - to_point.y
            return math.sqrt(dx ** 2 + dy ** 2)
        else:
            raise ValueError

    def get_angle(self, to_point):
        # 1. Prüft, ob to_point vom Typ Point ist
        # 2. Falls ja: Berechnet den Winkel, der eine Linie vom Punkt zu to_point gegenüber der X-Achse hat
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # Tipp 1: math.degrees(..) konvertiert von Radian zu Grad
        # Tipp 2: math.atan2(..) rechnet den Arcus-Tangenz
        if isinstance(to_point, Point):
            return math.degrees(math.atan2(to_point.y - self.y, to_point.x - self.x))
        else:
            raise ValueError

    def get_angle2points(self, p1, p2):
        # 1. Prüft, ob p1 un p2 vom Typ Point sind
        # 2. Falls ja: Berechnet den Winkel P1-SELF-P2 (also den Winkel, den die Strecken P1-SELF und SELF-P2 einfassen).
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # 4. Gibt IMMER die positive Variante des Winkels zurück (z.B. wenn Winkel = -45 --> Rückgabewert = 360 - 45 = 315)
        # Tipp 1: math.degrees(..) konvertiert von Radian zu Grad
        # Tipp 2: math.atan2(delta_y, delta_x) rechnet den Arcus-Tangenz
        if isinstance(p1, Point) and isinstance(p2, Point):
            angle = self.get_angle(p2) - self.get_angle(p1)
        else:
            raise ValueError
        if angle < 0:
            return 360 + angle
        else:
            return angle

    @ staticmethod
    def get_rand_point():
        p = Point()
        p.randomize()
        return p

    @staticmethod
    def onSegment(p, q, r) -> bool:
        # Given three collinear points p, q, r,
        # the function checks if point q lies
        # on line segment 'pr'
        if not (isinstance(p, Point) and isinstance(q, Point) and isinstance(r, Point)):
            raise ValueError

        if ((q.x <= max(p.x, r.x)) and
            (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and
                (q.y >= min(p.y, r.y))):
            return True
        else:
            return False

    @staticmethod
    def orientation(p, q, r) -> int:
        # To find orientation of ordered triplet (p, q, r).
        # The function returns following values
        # 0 --> p, q and r are collinear
        # 1 --> Clockwise
        # 2 --> Counterclockwise
        if not (isinstance(p, Point) and isinstance(q, Point) and isinstance(r, Point)):
            raise ValueError

        val = (((q.y - p.y) *
                (r.x - q.x)) -
               ((q.x - p.x) *
                (r.y - q.y)))

        if val == 0:
            return 0
        if val > 0:
            return 1  # Collinear
        else:
            return 2  # Clock or counterclock

    @staticmethod
    def doIntersect(p1, q1, p2, q2):

        if not (isinstance(p1, Point) and isinstance(q1, Point) and isinstance(p2, Point) and isinstance(q2, Point)):
            raise ValueError

        # Find the four orientations needed for
        # general and special cases
        o1 = Point.orientation(p1, q1, p2)
        o2 = Point.orientation(p1, q1, q2)
        o3 = Point.orientation(p2, q2, p1)
        o4 = Point.orientation(p2, q2, q1)

        # General case
        if (o1 != o2) and (o3 != o4):
            return True

        # Special Cases
        # p1, q1 and p2 are collinear and
        # p2 lies on segment p1q1
        if (o1 == 0) and (Point.onSegment(p1, p2, q1)):
            return True

        # p1, q1 and p2 are collinear and
        # q2 lies on segment p1q1
        if (o2 == 0) and (Point.onSegment(p1, q2, q1)):
            return True

        # p2, q2 and p1 are collinear and
        # p1 lies on segment p2q2
        if (o3 == 0) and (Point.onSegment(p2, p1, q2)):
            return True

        # p2, q2 and q1 are collinear and
        # q1 lies on segment p2q2
        if (o4 == 0) and (Point.onSegment(p2, q1, q2)):
            return True

        return False

    def __repr__(self):
        return f"({self.x}/{self.y})"

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, factor):
        return Point(self.x * factor, self.y * factor)

    def __truediv__(self, factor):
        return Point(self.x / factor, self.y / factor)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Polygon:
    class InvalidPolynomError(Exception):
        def __init__(self, message):
            super().__init__(message)

    INT_MAX = 1e21

    def __init__(self):
        # Erstellt eine leere Liste namens 'points' als Attribut
        self.points = []
        pass

    def add_point(self, point):
        # 1. Überprüft, ob point vom Typ Point ist
        # 2. Falls ja: Fügt der Liste 'points' den Punkt 'point' hinzu (Tipp: .append(...))
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise ValueError
        pass

    def get_n(self):
        # Gibt zurück, wie viele Ecken das Polygon hat
        return len(self.points)

    def get_num_points(self):
        return self.get_n()

    def clear_points(self):
        # Löscht alle gespeicherten Punkte
        self.points = []
        pass

    def get_sides(self):
        # Gibt eine Liste mit allen Seiten(längen) zurück.
        sides = []
        for i, point in enumerate(self.points):
            sides.append(point.get_distance(
                self.points[(i + 1) % len(self.points)]))
        return sides

    def get_circumference(self):
        # Berechnet den Umfang des Polygons
        # (Summiert alle Seitenlängen)
        return sum(self.get_sides())

    def get_longest_side(self):
        # Findet die längste Seite des Polygons und gibt sie zurück
        s = []
        for i, point in enumerate(self.points):
            s.append(point.get_distance(self.points[i - 1]))
        return max(s)

    def get_inside_angles(self):
        # Berechnet alle Innenwinkel des Polygons, also jeweils bei bei jedem Punkt der Winkel zw. den anliegenden Seiten,
        # und gibt eine Liste mit all diesen Winkeln zurück.
        # Tipp: Mit welcher Funktion lässt sich der Winkel zw. drei Punkten berechnen?
        # Achtung: Je nach dem in welche Richtung das Polygon dreht kriegen Sie die Aussenwinkel.
        # Mit der Formel sum(alle_winkel) = (n - 2) * 180 können Sie überprüfen, ob es sich um Innenwinkel handelt. Falls nicht, machen Sie daraus Innenwinkel.
        angles = []
        for i, point in enumerate(self.points):
            angles.append(point.get_angle2points(
                self.points[i - 1], self.points[(i + 1) % len(self.points)]))
        if sum(angles) == (self.get_n() - 2) * 180:
            # Sind Innenwinkel
            return angles
        else:
            inv_angles = []
            for angle in angles:
                inv_angles.append(360 - angle)
            if sum(inv_angles) == (self.get_n() - 2) * 180:
                # Check if it's a non-complex polygon
                return inv_angles
            else:
                # Has to be complex, so can't differ inner from outer angles
                return None

    def get_polygon_type(self):
        # ZUSATZAUFGABE
        # Überprüft, ob das Polygon regulär, konvex, konkav oder überschlagen (complex) ist.
        # Regulär: Alle Seiten gleich lang und alle Winkel gleich gross.
        # Konvex: Alle Innenwinkel sind <= 180 Grad
        # Konkav: Mindestens ein Innenwinkel ist > 180 Grad
        # Überschlagen: Funktion "get_inside_angles" gibt "None" zurück.
        # return 0: regulär
        #        1: konvex aber nicht regulär
        #        2: konkav
        #        3: überschlagen (complex)
        # Schwierigkeit: EASY
        angles = self.get_inside_angles()
        if angles == None:
            return 3  # überschlagen
        for angle in angles:
            if angle > 180:
                return 2  # konkav
        sides = self.get_sides()
        if min(sides) == max(sides) and min(angles) == max(angles):
            return 0  # regulär
        else:
            return 1  # konvex

    def has_unique_points(self):
        # ZUSATZAUFGABE
        # Überprüft, ob alle Punkte des Polygons einzigartig sind (also ob es keinen Punkt zwei Mal gibt)
        # Schwierigkeit: MEDIUM
        for i, point in enumerate(self.points):
            for j in range(i, len(self.points)):
                if i != j:
                    if point == self.points[j]:
                        return False
        return True

    def get_area(self):
        # ZUSATZAUFGABE
        # Berechnet die Fläche des Polyons
        # Schwierigkeit: MEDIUM
        # Tipp: Gaussche Trapezformel, geht für konvexe, koncave und komplexe Polygone.
        sum = 0
        for i in range(1, self.get_n()):
            sum += self.points[i].y * (self.points[i - 1].x -
                                       self.points[(i + 1) % len(self.points)].x)
        return abs(0.5 * sum)

    # Returns true if the point p lies
    # inside the polygon[] with n vertices

    def is_inside(self, p) -> bool:
        # ZUSATZAUFGABE
        # Source: https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
        # Überprüft, ob Punkt point innerhalb es Polygons liegt
        # Schwierigkeit: EXTREMELY HARD

        if not isinstance(p, Point):
            raise ValueError

        n = len(self.points)
        p = p

        # There must be at least 3 vertices
        # in polygon
        if n < 3:
            return False

        # Create a point for line segment
        # from p to infinite
        extreme = Point(self.INT_MAX, p.y)

        # To count number of points in polygon
        # whose y-coordinate is equal to
        # y-coordinate of the point
        decrease = 0
        count = i = 0

        while True:
            next = (i + 1) % n

            if(self.points[i].y == p.y):
                decrease += 1

            # Check if the line segment from 'p' to
            # 'extreme' intersects with the line
            # segment from 'polygon[i]' to 'polygon[next]'
            if (Point.doIntersect(self.points[i],
                                  self.points[next],
                                  p, extreme)):

                # If the point 'p' is collinear with line
                # segment 'i-next', then check if it lies
                # on segment. If it lies, return true, otherwise false
                if Point.orientation(self.points[i], p,
                                     self.points[next]) == 0:
                    return Point.onSegment(self.points[i], p,
                                           self.points[next])

                count += 1

            i = next

            if (i == 0):
                break

        # Reduce the count by decrease amount
        # as these points would have been added twice
        count -= decrease

        # Return true if count is odd, false otherwise
        return (count % 2 == 1)


# poly = Polygon()
# A = Point(0, 0)
# B = Point(2, 0)
# C = Point(2.5, 2.5)
# D = Point(0, 10.5)
# E = Point(-1, 2)
# poly.add_point(A)
# poly.add_point(E)
# poly.add_point(D)
# poly.add_point(C)
# poly.add_point(B)

# print(f"{poly.get_inside_angles() = }")
# print(f"{poly.is_convex() = }")
# print(f"{poly.get_area() = }")

# complex_poly = Polygon()
# complex_poly.add_point(Point(4.2, 0.2))
# complex_poly.add_point(Point(5.8, 0.2))
# complex_poly.add_point(Point(4, 2))
# complex_poly.add_point(Point(5.8, 1.8))

# print(f"{complex_poly.get_inside_angles() = }")
# print(f"{complex_poly.get_area() = }")
# print(poly.has_unique_points())
# print(poly.points[1] - poly.points[2])
# print(poly.points[1] * 10)

# n = 1000
# n_eck = Polygon()
# for i in range(0, n):
#     n_eck.add_point(Point(0, i))

# start = time.time()
# print(n_eck.has_unique_points())
# end = time.time()
# print(f"Took {round(end - start, 3)}s")


# print(f"Inside?: {poly.is_inside(Point(2.2, 1))}")


# Testpunkt
# print("### POINT-TESTS ###")
# p1 = Point(0, 0)
# p2 = Point(-1, 0)
# p3 = Point(0, 1)
# print(f"{p1.get_angle2points(p2,p3) = }")
# print(f"{p3.get_angle2points(p1,p2) = }")
# print(f"{p2.get_angle2points(p1,p3) = }")
