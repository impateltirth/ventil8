#!/usr/bin/env python3
"""
Equal-friction duct sizer for round galvanized-steel ducts (IP units).

Method: pick a design friction rate (in.wg per 100 ft, typically 0.08-0.10
for commercial low-velocity systems), then select the smallest standard
round duct diameter whose friction loss at the given airflow is at or
below it. Friction factor from the Haaland approximation; air at standard
density (0.075 lbm/ft^3).

This is a simplified sizer for preliminary/layout work. Verify final
selections against ASHRAE Fundamentals fitting loss coefficients.

Usage:
    python3 duct_sizing.py --cfm 1000 --length 40 --fittings elbow_90=2,diffuser=1
    python3 duct_sizing.py --example
"""

import argparse
import math

RHO = 0.075          # lbm/ft^3, standard air
NU_FT2_S = 1.69e-4  # ft^2/s, kinematic viscosity ~68 F
GC = 32.2            # lbm-ft/lbf-s^2
PSF_PER_INWG = 5.202
ROUGHNESS_FT = 0.0003  # galvanized steel

STANDARD_DIA_IN = [4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20,
                   22, 24, 26, 28, 30, 32, 34, 36]

# Rule-of-thumb equivalent straight-duct lengths (ft). Use ASHRAE fitting
# loss coefficients for final design.
FITTING_LEQ_FT = {
    "elbow_90": 25,
    "elbow_45": 12,
    "tee_branch": 40,
    "tee_main": 15,
    "damper": 10,
    "diffuser": 15,
    "grille": 10,
}

VEL_WARN_FPM = 1800  # flag velocities above typical low-velocity practice


def friction_rate(cfm, dia_in):
    """Return (in.wg per 100 ft, velocity fpm) for round duct."""
    d_ft = dia_in / 12.0
    area = math.pi * d_ft ** 2 / 4.0
    v_fpm = cfm / area
    v_fts = v_fpm / 60.0
    re = v_fts * d_ft / NU_FT2_S
    rel_rough = ROUGHNESS_FT / d_ft
    inv_sqrt_f = -1.8 * math.log10((rel_rough / 3.7) ** 1.11 + 6.9 / re)
    f = 1.0 / inv_sqrt_f ** 2
    dp_psf = f * (100.0 / d_ft) * (RHO * v_fts ** 2) / (2 * GC)
    return dp_psf / PSF_PER_INWG, v_fpm


def size_duct(cfm, target_fr=0.08):
    """Smallest standard diameter with friction rate <= target.

    Returns (diameter_in, actual_fr, velocity_fpm, over_target).
    """
    for d in STANDARD_DIA_IN:
        fr, v = friction_rate(cfm, d)
        if fr <= target_fr:
            return d, fr, v, False
    d = STANDARD_DIA_IN[-1]
    fr, v = friction_rate(cfm, d)
    return d, fr, v, True


def parse_fittings(spec):
    """'elbow_90=2,diffuser=1' -> [('elbow_90', 2), ...]."""
    out = []
    if not spec:
        return out
    for item in spec.split(","):
        name, _, count = item.partition("=")
        name = name.strip()
        if name not in FITTING_LEQ_FT:
            raise ValueError("unknown fitting '%s' (known: %s)"
                             % (name, ", ".join(sorted(FITTING_LEQ_FT))))
        out.append((name, int(count)))
    return out


def size_segment(name, cfm, length_ft, fittings, target_fr=0.08):
    dia, fr, vel, over = size_duct(cfm, target_fr)
    leq = sum(FITTING_LEQ_FT[n] * c for n, c in fittings)
    total_len = length_ft + leq
    loss = fr / 100.0 * total_len
    print("%s: %d CFM" % (name, cfm))
    print("  duct: %d in round | velocity: %.0f fpm%s | friction: %.3f in.wg/100 ft%s"
          % (dia, vel,
             "  <-- HIGH VELOCITY" if vel > VEL_WARN_FPM else "",
             fr,
             "  <-- over target" if over else ""))
    print("  straight: %.0f ft + fittings: %.0f ft eq. = %.0f ft total"
          % (length_ft, leq, total_len))
    print("  segment loss: %.3f in.wg\n" % loss)
    return loss


def example():
    print("Illustrative workshop system (replace CFMs with your design values)\n")
    total = 0.0
    total += size_segment("Supply main", 1500, 40,
                          [("elbow_90", 2), ("tee_main", 1)])
    total += size_segment("Branch A (to diffusers)", 800, 25,
                          [("elbow_90", 1), ("diffuser", 2)])
    total += size_segment("Branch B (to diffusers)", 700, 30,
                          [("elbow_90", 1), ("diffuser", 2)])
    print("Worst-path total (main + longest branch): "
          "add the two in series for fan sizing.")


def main():
    ap = argparse.ArgumentParser(description="Equal-friction round duct sizer")
    ap.add_argument("--cfm", type=float, help="airflow in CFM")
    ap.add_argument("--length", type=float, default=0, help="straight duct length, ft")
    ap.add_argument("--fittings", default="",
                    help="e.g. elbow_90=2,diffuser=1")
    ap.add_argument("--target-fr", type=float, default=0.08,
                    help="design friction rate, in.wg/100 ft")
    ap.add_argument("--example", action="store_true",
                    help="run the illustrative workshop example")
    args = ap.parse_args()

    if args.example:
        example()
        return
    if not args.cfm:
        ap.error("--cfm is required (or use --example)")
    size_segment("Segment", args.cfm, args.length,
                 parse_fittings(args.fittings), args.target_fr)


if __name__ == "__main__":
    main()
