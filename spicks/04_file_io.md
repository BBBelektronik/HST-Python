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
**File IO**
Theorie mit Beispielen

To PDF: [Normal](pdfs/04_file_io.pdf), [Slides](pdfs/04_file_io_slides.pdf)

---

# Inhalt
- [Datei öffnen](#datei-öffnen)
- [CSV-Datei einlesen](#csv-datei-einlesen)
- [In Datei schreiben](#in-datei-schreiben)

---

## Datei öffnen
Try it yourself:
```python
file = open('filename.csv', 'r')
    f.read()
```

---
## CSV-Datei einlesen
Try it yourself:
```python
import csv
with open('filename.csv') as f:
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

## In Datei schreiben