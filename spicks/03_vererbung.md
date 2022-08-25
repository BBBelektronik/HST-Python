---
marp: true
author: Nico Schwab
theme: uncover
size: 16:9
paginate: true
# _paginate: false
_header: '![bbb_logo_svg w:150px](Logo_BBB_inv.svg)'
footer: HST @ BBB by ScN
class: invert
style: |
    header {
        text-align: right
    }

    footer {
        bottom: 10px
    }

    section {
        font-size: 33px
    }

---

# Python - OOP
**Vererbung (engl. Inheritance)**
Theorie mit Beispielen

To PDF: [Normal](pdfs/03_vererbung.pdf), [Slides](pdfs/03_vererbung_slides.pdf)

---

# Inhalt
- [Vererbung](#vererbung)
- [Begriffe](#begriffe)
- [~~Vererbung~~ Beispiel 1](#vererbung-beispiel-1)
- [Vererbung Beispiel 2](#vererbung-beispiel-2)
- [Vererbung Beispiel 3](#vererbung-beispiel-3)
- [UML Klassendiagramm](#uml-klassendiagramm)

---

## Vererbung
Klasse B erbt **alle** Eigenschaften von Klasse A.
Klasse B kann dann mit neuen Eigenschaften erweitert werden.

**Warum?**
- Existierende Klassen weiterverwenden
- Wiederholungen nur einmal programmieren

---

## Begriffe

| Erbende Klasse | Vererbende Klasse |
| :------------: | :---------------: |
| Derived Class  |    Base Class     |
|     Child      |      Parent       |
|   Subklasse    |    Superklasse    |

---

## ~~Vererbung~~ Beispiel 1
Keine Vererbung (normale Klasse)
```python
# Klasse Person
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name ist {self.name}")
    
# Instanz erstellen
p1 = Person("Seppli")

p1.display_name()
```
---

## Vererbung Beispiel 2
```python
# Klasse Person (Superklasse)
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name ist {self.name}")

# Klasse Apprentice (Subklasse)
class Apprentice(Person):  # <-- In Klammern ist die BaseClass
    def __init__(self, name):
        super().__init__(name) # <-- super().__init__(...) ruft Initializer der Superklasse

# Instanz erstellen
bl1 = Apprentice("Seppli")

bl1.display_name() # <-- Methode von Person
```

---
## Vererbung Beispiel 3
```python
# Klasse Person (Superklasse)
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name ist {self.name}")
    
# Klasse Apprentice (Subklasse)
class Apprentice(Person):
    def __init__(self, name, firma):
        super().__init__(name)
        self.firma = firma

    def display_info(self):
        print(f"{self.name} arbeitet bei {self.firma}.") 
        # self.name ^^^ ist von Superklasse

# Instanz erstellen
bl1 = Apprentice("Seppli", "SCS")

bl1.display_info()
```

---

## UML Klassendiagramm
Vererbung wird mit leerem Pfeil dargestellt.
Er zeigt von Sub- zu Superklasse (und nicht umgekehrt)!

![uml h:450px](uml_vererbung.png)