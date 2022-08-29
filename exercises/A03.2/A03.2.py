import math
import random


class Point:
    def __init__(self, x=0, y=0):
        # 1. Überprüft, ob x und y numerisch (also int oder float) sind.
        # 2. Speichert die Argumente x und y als öffentliche Attribute ab.
        pass

    def get_x(self):
        # Gibt die x-Koordinate des Punktes zurück
        pass

    def get_y(self):
        # Gibt die y-Koordinate des Punktes zurück
        pass

    def set_x(self, x):
        # 1. Überprüft, ob x numerisch ist.
        # 2. Falls ja: Speichert die x-Koordinate
        pass

    def set_y(self, y):
        # 1. Überprüft, ob y numerisch ist.
        # 2. Falls ja: Speichert die y-Koordinate
        pass

    def get_length(self):
        # Gibt die Distanz des Punktes vom Nullpunkt zurück (die "Länge" eines Punktes).
        # Tipp 1: Pythagoras
        # Tipp 2: Die Methode math.sqrt() von der Math-Library (import math) könnte hilfreich sein.
        pass

    def get_quadrant(self):
        # Gibt als Integer zurück, in welchem Quadranten des Koordinatensystems sich der Punkt befindet.
        # Gibt 0 zurück, wenn der Punkt sich genau auf einer Achse befindet.
        pass

    def randomize(self, max):
        # 1. Überprüft, ob 'max' ein numerischer Wert ist (int oder float)
        # 2. Falls ja: Generiert zufällige Werte für x und y (bis max) und speichert diese ab.
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # Tipp: Von random.randint(von, bis) bekommen Sie einen zufälligen Integer zw. 'von' und 'bis'
        pass

    def get_distance(self, to_point):
        # 1. Prüft, ob to_point vom Typ Point ist
        # 2. Falls ja: Berechnet die Distanz zwischen sich selber und einem anderen Punkt 'to_point' und gibt diese zurück.
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # Tipp: Die Methode math.sqrt() von der Math-Library (import math) könnte hilfreich sein.
        pass

    def get_angle(self, to_point):
        # 1. Prüft, ob to_point vom Typ Point ist
        # 2. Falls ja: Berechnet den Winkel, der eine Linie vom Punkt 'self' zum Punkt 'to_point' gegenüber der X-Achse hat
        #    Der Winkel wird in einem Koordinatensystem immer im Gegenuhrzeigersinn gemessen.
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        # Tipp 1: math.degrees(..) konvertiert von Radian zu Grad
        # Tipp 2: math.atan2(delta_y, delta_x) rechnet den Arcus-Tangenz
        pass


class Polygon:
    def __init__(self):
        # Erstellt eine leere Liste namens 'points' als Attribut
        pass

    def add_point(self, point):
        # 1. Überprüft, ob point vom Typ Point ist
        # 2. Falls ja: Hängt der Liste 'points' den Punkt 'point' an (Tipp: .append(...) = anhängen)
        # 3. Falls nein: Führt 'raise ValueError' aus (ohne Anführungszeichen)
        pass

    def get_num_points(self):
        # Gibt die Anzahl der eingegebenen Punkte zurück
        pass

    def clear_points(self):
        # Löscht alle gespeicherten Punkte
        pass

    def get_circumference(self):
        # Berechnet den Umfang des Polygons
        # (addiert also die Distanzen zw. P0 und P1, P1 und P2, ..., PN und P0)
        pass

    def get_longest_side(self):
        # Findet die längste Seite des Polygons und gibt sie zurück
        pass

    def has_unique_points(self):
        # ZUSATZAUFGABE
        # Überprüft, ob alle Punkte des Polygons einzigartig sind (also ob es keinen Punkt zwei Mal gibt)
        # Schwierigkeit: MIDDLE
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

    def is_inside(self, point):
        # ZUSATZAUFGABE
        # Überprüft, ob Punkt point innerhalb es Polygons liegt
        # Schwierigkeit: EXTREMELY HARD
        pass


# Hier wird der Code getestet! z.B.
p1 = Point(0, 0)
p2 = Point(0, 2)

# --> Distanz zw. (0/0) und (0/2) sollte 2 sein. VERIFIZIEREN!
print(p1.get_distance(p2))
