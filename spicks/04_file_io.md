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

# Python - File IO
Theorie mit Beispielen

To PDF: [Normal](pdfs/04_file_io.pdf), [Slides](pdfs/04_file_io_slides.pdf)

---

# Inhalt
- [Datei öffnen und schliessen](#datei-öffnen-und-schliessen)
- [File-Modi](#file-modi)
- [Ganze Datei ausgeben](#ganze-datei-ausgeben)
- [In Datei schreiben](#in-datei-schreiben)
- [CSV-Datei einlesen](#csv-datei-einlesen)
- [String aufteilen](#string-aufteilen)
- [Substring in String](#substring-in-string)
- [Noch mehr String-Methoden](#noch-mehr-string-methoden)

---

## Datei öffnen und schliessen
Eine geöffnete Datei muss immer geschlossen werden!
```python
file = open(filename, 'r')  # Open in read-only mode
print(file.read())          # Do something with file
file.close()                # Close file (important!)
```
Oder man verwendet `with`, da wird die Datei automatisch wieder geschlossen wenn der Block verlassen wird:
```python
with open(filename, 'r') as file:
    print(file.read())
``` 

---

## File-Modi
Die Funktion `open(filename, mode)` nimmt als zweiter Parameter (`mode`) verschiedene Modi.

Die wichtigsten ([es gibt noch mehr](https://www.geeksforgeeks.org/open-a-file-in-python/)):

| `mode` | Beschreibung    |
| ------ | --------------- |
| `'r'`  | Read            |
| `'w'`  | Write [1], [2]  |
| `'a'`  | Append [1], [3] |

[1] Erstellt die Datei falls nicht vorhanden.
[2] Überschreibt eine bestehende Datei!
[3] Hängt ans Ende einer Datei an falls vorhanden.

---

## Ganze Datei ausgeben
Ausgabe Zeile für Zeile
```python
with open(filename, 'r') as file:
    for line in file:
        print(line)
```

---

## In Datei schreiben
```python
# Öffnet eine Datei. Erstellt sie, falls nicht vorhanden
file = open(filename, 'w')

# Write characters
file.write("Hello File")
# Linebreak
file.write("Newline: \n")

# Write multiple lines from listfile
file.writelines(["line1", "line2", "..."])

# Close file (important!)
file.close()
```
oder natürlich auch mit `open(...)`:
```python
with open(filename, 'w') as file:
    ...
```

---
## CSV-Datei einlesen
Try it yourself:
```python
import csv
with open(filename) as f:
    csv_file = csv.reader(f)
    print(csv_file)
    # csv_file enthält den Dateiinhalt in einer
    # list-ähnlichen Struktur.
    # Kann wie eine Liste gelesen werden.
    # Bsp.:
    for line in csv_file:
        print(line)
```

---

## String aufteilen
`split()` trennt bei Whitespaces (Space, Tab, usw.)
`split('o')` trennt bei Zeichen, hier z.B. bei 'o'
```python
a_string = "ET wants to phone home"

print(a_string.split())     # --> ['ET', 'wants', 'to', 'phone', 'home']
print(a_string.split('o'))  # --> ['ET wants t', ' ph', 'ne h', 'me']

```

---

## Substring in String
Überprüfen, ob Sub-String in String drin ist.
```python
a_string = "ET wants to phone home"
if "phone" in a_string:
    print("Phone is in string") # <-- Das wird ausgeführt
else:
    print("Phone is not in string")
```

---

## Noch mehr String-Methoden
[Unter diesem Link](https://www.w3schools.com/python/python_ref_string.asp) finden Sie noch viele weitere String-Methoden. Nützlich sind unter anderem:
|                |              |
| -------------- | ------------ |
| `split()`      | `replace()`  |
| `startswith()` | `endswith()` |
| `upper()`      | `lower()`    |
| `split()`      | `replace()`  |
