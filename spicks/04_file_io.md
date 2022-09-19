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

---

## Datei öffnen und schliessen
Eine geöffnete Datei muss immer geschlossen werden!
```python
file = open(filename, 'r')  # Open in read-only mode
print(file.read())          # Do something with file
file.close()                # Close file (important!)
```
Or use `with` for automatic closing of file:
```python
with open(filename, 'r') as file
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
