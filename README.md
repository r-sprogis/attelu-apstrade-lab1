# Attēlu Apstrāde - Lab 1
Projekts demonstrē četrus attēlu jaukšanas režīmus

## Uzstādīšana
```pip install -r requirements.txt```

## Lietošana
Palaid:
```python main.py```

Rezultāti tiks saglabāti kā PNG faili:
- `darken.png` — tumšināšana (katram pikselim izvēlas mazāko vērtību)
- `screen.png` — ekrāns (invertē, reizina, invertē atpakaļ)
- `linear_dodge.png` — lineārā izvairīšanās (saskaita pikseļu vērtības)
- `hard_light.png` — cietā gaisma (kombinē reizināšanu un ekrānu)
