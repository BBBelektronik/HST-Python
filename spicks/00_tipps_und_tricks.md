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

section {
    font-size: 33px
}
</style>

# Python - Tipps & Tricks
Verschiedene Tricks und hilfreiche Sachen in Python

---

## Stringformatierung
Strings mit Variablen lassen sich geschickt formatieren, try it:
```python
s = "hi"
i = 4
h = 0x20

print(f"str: {s}; int: {i}; hex: {h:#x}")
```
Oder man nutzt Abkürzungen, try it:
```python
x = 22
print(f"{x = }")
```

---

## Strings und Zahlen einlesen
`input()` gibt einen String zurück. Deshalb braucht es Konvertierungsfunktionen wie `int()` und `float()`.
Try it out:
```python
# String einlesen
a_string = input("Enter a string: ")
print(a_string)

# Integer einlesen
an_integer = int(input("Enter an integer: "))
print(an_integer)

# Float einlesen
a_float = float(input("Enter a float: "))
print(a_float)
```

---

## Namenskonventionen
1. Kollaboration wird einfacher
2. Verständlichkeit der Software wird besser

z.B.
```python
counter = 0     # Variablen klein
avg_volt = 12   # Mit _ trennen
update()        # Funktionsnamen klein
get_age()       # Mit _ trennen
MAX_V = 500     # Konstanten GROSS
```

---

## Zahlen mit versch. Basen
In Python lassen sich einfach Zahlen in verschiedenen Zahlensystemen eingeben.
```python
dezimal = 4                         # base 10
hexadez = 0x20                      # base 16
binaer  = 0b100101                  # base 2
oktal   = 0o23327                   # base 8
n_tal   = int("123456789", base=n)  # base n (frei wählbar)
```