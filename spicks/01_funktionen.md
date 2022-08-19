---
marp: true
author: Nico Schwab
theme: uncover
size: 16:9
paginate: true
_paginate: false
_header: '![bbb_logo_svg w:150px](Logo_BBB.svg)'
footer: HST | Nico Schwab | BBB | nico.schwab@bbbaden.ch
---

<style>
header {
    text-align: right
}

footer {
    bottom: 10px
}

/* h2 {
    font-size: 55px
} */
</style>

# Python - Funktionen
Theorie mit Beispielen

---

## Wieso Funktionen?
- **Information** > Funktionsname beschreibt, was passiert
- **Struktur** > Programm wird in kleine Häppchen aufgeteilt
- **Wiederverwendbarkeit** > Zu wiederholende Aufgaben müssen nur ein Mal programmiert werden 

---

## Syntax
![syntax w:1000](funktionen_syntax.png)

---

## Definition und Aufruf
Try it out:
```python
def sayHello(name, place):
    print(f'Hello {name} from {place}')

sayHello('Din Djarin', 'Mandolor')

# Was ist der Output?
```

---


## Rückgabewerte
```python
# One return value
def a_function(number):
    return number * 2

# or multiple return values

def another_function(bla, blib):
    # do something to bla and blib
    return bla, blib
```

---

## Defaultwerte
Try it out:
```python
def mult3(n1, n2=5, n3=1):
    return n1 * n2 * n3

print(mult3(4))
print(mult3(4, 2))
print(mult3(4, n3=2))

# Was ist der Output?
```
---

## Variablen Geltungsbereich (Scope)
Try it out:
```python
def scopeDemo():
    x = 10
    print(f"inside of ScopeDemo(): \t {x = }")
    
x = 20
scopeDemo()
print(f"outside of ScopeDemo(): \t {x = }")

# Was ist der Output?
```

---

## Funktionen in Funktionen in ...
Try it out:
```python
def outer(): # Definition outer()

    def inner(): # Definition inner()
        print("inner") # Inhalt inner()

    print("outer") # Inhalt outer()

    inner() # Aufruf inner()

outer() # Aufruf outer()

# Was ist der Output?
```
