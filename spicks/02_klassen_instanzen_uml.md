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
**Klassen, Instanzen, UML**
Theorie mit Beispielen

To PDF: [Normal](pdfs/02_klassen_instanzen_uml.pdf), [Slides](pdfs/02_klassen_instanzen_uml_slides.pdf)

---

# Inhalt
- [OOP?](#oop)
- [!OOP vs. OOP](#oop-vs-oop)
- [Zugriff auf Attribut/Methode](#zugriff-auf-attributmethode)
- [Klasse mit Attribut](#klasse-mit-attribut)
- [Klasse mit Methode](#klasse-mit-methode)
- [Klasse Beispiel](#klasse-beispiel)
- [private vs. public](#private-vs-public)
- [Beispiel private/public Attribute](#beispiel-privatepublic-attribute)
- [Beispiel private/public Methoden](#beispiel-privatepublic-methoden)
- [Instanz- und Klassenattribute](#instanz--und-klassenattribute)
- [Instanz-/Klassenattribute Beispiel](#instanz-klassenattribute-beispiel)
- [UML Klassendiagramm](#uml-klassendiagramm)

---

## OOP?
- **OOP** > Objektorientierte Programmierung
- **Objekte** > Objekte sind Datenkonstrukte, die Attribute und/oder Methoden enthalten
  - **Alles ist ein Objekt in Python!** (auch z.B. `int`, `str`, ...)
- **Klassen** > Baupläne für Objekte
- **Instanzen** > Eine Objekt gebaut nach einem Bauplan (Klasse)
  - "Eine Instanz einer Klasse" 

---

## !OOP vs. OOP

|   !OOP   |   OOP    |
| :------: | :------: |
| Variable | Attribut |
| Funktion | Methode  |

---

## Zugriff auf Attribut/Methode
-> `.` <-

z.B.
```python
instanz.attribut
# oder
instanz.methode()
```
---

## Klasse mit Attribut
Try it yourself:
```python
# Klasse mit Initialiser (vgl. Konstruktor bei C++)
class ClassWithAttribut:
    # Die Methode __init__(self) ist der Initialiser
    def __init__(self): # <-- self muss immer rein
        self.attribut = "z.B. ein String"

# Instanz erstellen
instance = ClassWithAttribut()

# Auf Attribut zugreifen und dieses ausgeben
print(instance.attribut)
```
`self` ist eine Referenz auf sich selber (vgl. `this` in `C++` oder Java)

---

## Klasse mit Methode
Try it yourself:
```python
# Klasse mit Initialiser (vgl. Konstruktor bei C++)
class ClassWithMethod:
    def say_hi(self): # <-- das 'self' macht es zu einer Methode
        print('hi')

# Instanz erstellen
instance = ClassWithMethod()

# Methode ausführen
instance.say_hi()
```

---

## Klasse Beispiel
Try it yourself:
```python
# Klasse definieren
class Person:
    def __init__(self, name, age):
    self._name = name
    self._age = age

    # Methode definieren
    def greet(self):
        print(f"Hi {self._age} year old {self._name}")

# Instanz erstellen (mit Argument)
john = Person("John", 37)

# Methode ausführen
john.greet()
```

---

## private vs. public
Definiert die Zugriffsregelung von Attributen und Methoden eines Objektes.
|                     |             private              | public                             |
| :-----------------: | :------------------------------: | ---------------------------------- |
| **Zugriff erlaubt** | **nur** innerhalb einer Instanz. | **auch** ausserhalb einer Instanz. |
|    **Attribut**     |           `_attribut`            | `attribut`                         |
|     **Methode**     |          `_method(...)`          | `method(...)`                      |

---

## Beispiel private/public Attribute
```py
class A:
    def __init__(self):
        self.public_attr    = "public Attribut"
        self._private_attr  = "private Attribut"

    def get_private(self):
        return self._private_attr

a = A()
print(a.public_attr) # OK
print(a._private_attr) # NOT OK! Why?
print(a.get_private()) # OK! Why?
```

---
## Beispiel private/public Methoden

```py
class A:
    def foo(self):
        print("I am public!")

    def _fuu(self):
        print("I am private: Don't touch this!")

a = A()
a.foo() # OK
a._fuu() # NOT OK! Why?
```

---

## Instanz- und Klassenattribute

- **Instanzattribut:** Jede Instanz einer Klasse hat ihr eigenes Attribut
- **Klassenattribut:** **ALLE** Instanzen einer Klasse **TEILEN** das gleiche Attribut

```py
class A:
    # Klassenattribute hier
    ...
    def __init__(self):
        # Instanzattribute hier
        ...
```

---

## Instanz-/Klassenattribute Beispiel
Try it yourself:
```py
class BBBStudent:
    count = 0    # Klassenattribut
    def __init__(self, name):
        BBBStudent.count += 1
        self.name = name # Instanzattribut
    
student1 = BBBStudent("Jan")
print(BBBStudent.count)

student2 = BBBStudent("Olivier")
print(BBBStudent.count)
```

---

## UML Klassendiagramm
- **UML** > Unified Modeling Language
- **Klassendiagramm** > Gibt eine Übersicht über Programmstruktur

![uml h:300px](uml_klasse.png)

*Dies ist das Klassendiagramm des [Klassenbeispiels](#klasse-beispiel).*