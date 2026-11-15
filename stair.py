#!/usr/bin/env python3
"""Stair geometry for Part 3 exit stairs: risers, treads and total run."""
import argparse, math

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--total-rise-mm", type=float, required=True)
    p.add_argument("--tread-mm", type=float, default=280)
    a = p.parse_args()
    n = math.ceil(a.total_rise_mm / 200)
    riser = a.total_rise_mm / n
    while riser < 125 and n > 1:
        n -= 1; riser = a.total_rise_mm / n
    treads = n - 1
    run_total = treads * a.tread_mm
    print(f"Total rise {a.total_rise_mm:g} mm -> {n} risers of {riser:.1f} mm each")
    print(f"Riser check (125-200 mm): {'OK' if 125 <= riser <= 200 else 'OUT OF RANGE'}")
    print(f"Treads: {treads} x {a.tread_mm:g} mm -> total run {run_total:.0f} mm ({run_total / 1000:.2f} m), excluding landings")
    print(f"Tread check (min 250 mm for exit stairs): {'OK' if a.tread_mm >= 250 else 'TOO NARROW'}")
    print(f"Comfort guide 2R + T = {2 * riser + a.tread_mm:.0f} mm (guidance range about 570-660 mm)")
    print("Exit stairs: minimum 1,100 mm clear between handrails. Dwelling-unit stairs use Part 9 limits instead.")

if __name__ == "__main__":
    main()
