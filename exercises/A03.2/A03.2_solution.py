import math
import random
import time


class Point:
    def __init__(self, x=0, y=0):
        # 1. Überprüft, ob x und y numerisch (also int oder float) sind.
        # 2. Speichert die Argumente x und y als öffentliche Attribute ab.
        self.x = x if isinstance(x, (int, float)) else 0
        self.y = y if isinstance(y, (int, float)) else 0
        pass

    def get_x(self):
        # Gibt die x-Koordinate des Punktes zurück
        return self.x
        pass

    def get_y(self):
        # Gibt die y-Koordinate des Punktes zurück
        return self.y
        pass

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
        pass

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
        pass

    @ staticmethod
    def get_rand_point():
        p = Point()
        p.randomize()
        return p

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

    def get_num_points(self):
        # Gibt die Anzahl der eingegebenen Punkte zurück
        return len(self.points)
        pass

    def clear_points(self):
        # Löscht alle gespeicherten Punkte
        self.points = []
        pass

    def get_circumference(self):
        # Berechnet den Umfang des Polygons
        # (addiert also die Distanzen zw. P0 und P1, P1 und P2, ..., PN und P0)
        circ = 0
        for i, point in enumerate(self.points):
            circ += point.get_distance(self.points[i - 1])
        return circ
        pass

    def get_longest_side(self):
        # Findet die längste Seite des Polygons und gibt sie zurück
        s = []
        for i, point in enumerate(self.points):
            s.append(point.get_distance(self.points[i - 1]))
        return max(s)
        pass

    def has_unique_points(self):
        # ZUSATZAUFGABE
        # Überprüft, ob alle Punkte des Polygons einzigartig sind (also ob es keinen Punkt zwei Mal gibt)
        # Schwierigkeit: MIDDLE
        for i, point in enumerate(self.points):
            for j in range(i, len(self.points)):
                if i != j:
                    if point == self.points[j]:
                        return False
        return True
        pass

    def get_area(self):
        # ZUSATZAUFGABE
        # Berechnet die Fläche des Polyons (angenommen, es ist ein reguläres Polygon)
        # Tipp: Dreiecke
        # Schwierigkeit: HARD
        pass

    def is_regular(self):
        # ZUSATZAUFGABE
        # Überprüft, ob das Polygon ein reguläres Polygon ist
        # Schwierigkeit: VERY HARD
        pass

    def is_point_in_polygon(self, point):
        # ZUSATZAUFGABE
        # Überprüft, ob Punkt point innerhalb es Polygons liegt
        # Schwierigkeit: EXTREMELY HARD
        pass


viereck = Polygon()
viereck.add_point(Point(0, 0))
viereck.add_point(Point(0, 2))
viereck.add_point(Point(2, 2))
viereck.add_point(Point(2, 0))

# print(viereck.get_circumference())
# print(viereck.has_unique_points())
# print(viereck.points[1] - viereck.points[2])
# print(viereck.points[1] * 10)

n = 1000
n_eck = Polygon()
for i in range(0, n):
    n_eck.add_point(Point(0, i))

start = time.time()
print(n_eck.has_unique_points())
end = time.time()
print(f"Took {round(end - start, 3)}s")
