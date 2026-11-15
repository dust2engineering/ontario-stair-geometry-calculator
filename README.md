# Ontario Stair Geometry Calculator

Works out a Part 3 exit stair: from the floor-to-floor rise it chooses the number of risers so every riser sits inside the Ontario Building Code range of 125-200 mm, keeps all risers equal, and totals the tread run (treads at least 250 mm).

**Live web tool:** https://dust2engineering.github.io/ontario-stair-geometry-calculator/web/

## How it works

- Riser count = ceiling of total rise / 200 mm, adjusted so the equal riser is not below 125 mm.
- Total run = (risers - 1) x tread run, excluding landings.

## Data in this repository

- stair-data.json — the governing limits and guidance values, machine-readable.

## Command line

```bash
python3 stair.py --total-rise-mm 3200 --tread-mm 280
```

## Worked examples

- [floor-3200mm.md](examples/floor-3200mm.md)
- [floor-2800mm.md](examples/floor-2800mm.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Building general. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
