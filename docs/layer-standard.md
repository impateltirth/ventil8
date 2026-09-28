# CAD layer standard

Layer scheme for the Ventil8 AutoCAD drawings. **TODO:** align names/colors with the actual DWG — update this table to match.

## HVAC layers

| Layer | Color | Linetype | Contents |
|---|---|---|---|
| `V-HVAC-DUCT-SUPP` | Cyan (4) | Continuous | Supply ductwork, double-line |
| `V-HVAC-DUCT-EXHS` | Magenta (6) | Continuous | Exhaust ductwork, double-line |
| `V-HVAC-DUCT-CNTR` | Red (1) | Center | Duct centerlines (schematic views) |
| `V-HVAC-DIFF` | Green (3) | Continuous | Diffusers, grilles, registers |
| `V-HVAC-EQPM` | Yellow (2) | Continuous | Fans, AHUs, equipment connections |
| `V-HVAC-DMPR` | White (7) | Continuous | Dampers, access doors |
| `V-HVAC-FLOW` | Cyan (4) | Dashed | Airflow direction arrows |
| `V-HVAC-TEXT` | White (7) | Continuous | Labels, CFM tags, duct sizes |
| `V-HVAC-DIMS` | White (7) | Continuous | Dimensions |

## Architectural background (xref)

| Layer | Color | Contents |
|---|---|---|
| `A-WALL` | 8 (grey) | Walls (screened back) |
| `A-DOOR` | 8 (grey) | Doors, openings |
| `A-GRID` | 9 (light grey) | Column grid |

## Conventions

- Model Space: full-scale geometry (1 unit = 1 inch, or 1 unit = 1 mm — **TODO: record yours**).
- Paper Space: one layout per sheet, scaled viewports (floor plans typically 1/4" = 1'-0"), title block with sheet number.
- Duct sections cut at 1/2" = 1'-0" or larger; installation callouts on `V-HVAC-TEXT`.
