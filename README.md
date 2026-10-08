# Ventil8

[![Test duct sizing](https://github.com/impateltirth/ventil8/actions/workflows/test.yml/badge.svg)](https://github.com/impateltirth/ventil8/actions/workflows/test.yml)

Ventilation layout for a small manufacturing workshop, drafted in AutoCAD: supply/exhaust duct routing, diffuser locations, equipment connections, and airflow schematics across drawing layers — with Paper Space construction drawings (scaled floor plans, duct section details, installation callouts).

**Stack:** AutoCAD · Mechanical drafting · Schematics

## What's here

| Path | Contents |
|---|---|
| `tools/duct_sizing.py` | Equal-friction round-duct sizer (IP units): airflow in → duct diameter, velocity, friction loss, fitting losses |
| `docs/design-basis.md` | Design values template: ACH, CFM schedule, duct schedule |
| `docs/layer-standard.md` | CAD layer scheme for the drawing set |
| `docs/drawing-index.md` | Sheet index (M-001…) |
| `docs/system-schematic.md` | Conceptual supply/exhaust airflow diagram |
| `cad/` | Export drop-point for sheet PDFs / DWG |

## Duct sizing

```bash
python3 tools/duct_sizing.py --cfm 1000 --length 40 --fittings elbow_90=2,diffuser=1
python3 tools/duct_sizing.py --example   # illustrative workshop system
```

Equal-friction method at 0.08 in.wg/100 ft (adjustable): picks the smallest standard round duct at or below the target friction rate, reports velocity (flags > 1800 fpm), and totals straight + fitting-equivalent lengths into a segment pressure loss. Simplified for layout work — verify final selections against ASHRAE fitting coefficients.

## Status

- [x] Equal-friction duct sizing tool (tested: 1000 CFM → 16" @ 0.046 in.wg/100 ft)
- [x] Layer standard, drawing index, design-basis templates
- [ ] Real design values (area, ACH, CFM schedule) in `docs/design-basis.md`
- [ ] Align `docs/layer-standard.md` with the actual DWG layers
- [ ] Exported sheet PDFs in `cad/`

## License

MIT — see [LICENSE](LICENSE).
