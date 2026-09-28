# Design basis — Ventil8

Ventilation layout for a small manufacturing workshop: supply/exhaust duct routing, diffuser locations, equipment connections, and airflow schematics, drafted in AutoCAD across drawing layers, with Paper Space construction drawings (scaled floor plans, duct sections, installation callouts).

## TODO: fill in the design values from the project

| Item | Value | Notes |
|---|---|---|
| Workshop floor area | | ft² |
| Ceiling height | | ft |
| Design air changes per hour (ACH) | | |
| Supply airflow (total) | | CFM |
| Exhaust airflow (total) | | CFM |
| Make-up air strategy | | |
| Filtration level | | e.g. MERV rating |
| Heating/cooling equipment | | connections shown on plan |
| Design friction rate | 0.08 in.wg/100 ft | used in `tools/duct_sizing.py` |

## Airflow summary — TODO

| Zone / room | Supply (CFM) | Exhaust (CFM) | Diffusers | Notes |
|---|---|---|---|---|
| | | | | |

## Duct schedule — TODO

Export or transcribe the final schedule here (or keep it on the drawings):

| Segment | CFM | Duct size | Velocity (fpm) | Loss (in.wg) |
|---|---|---|---|---|
| | | | | |

Generate the sizes with:

```bash
python3 tools/duct_sizing.py --cfm 1000 --length 40 --fittings elbow_90=2,diffuser=1
python3 tools/duct_sizing.py --example   # illustrative system
```
