# Aufgabenblatt 1

## A.1
Bei Smartphones eines bestimmten Herstellers wurden bei 1000 Geräten folgende Lebensdauer (in Monaten) des Displays festgestellt:

| Lebensdauer   | <= 6 Monate | 6-12 Monate | 12-18 Monate | 18-24 Monate | 24-30 Monate |
|---------------|-------------|-------------|--------------|--------------|--------------|
| Anzahl Geräte | 33          | 276         | 404          | 237          | 50           |

Stellen Sie die Häufigkeitsverteilung und die Summenhäufigkeitsverteilung (absolut und relativ) dar.

### Antwort
**Häufigkeitsverteilung**

```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "data": {"url": "data/seattle-weather.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"timeUnit": "month", "field": "date", "type": "ordinal"},
    "y": {"aggregate": "mean", "field": "precipitation", "type": "quantitative"}
  }
}
```