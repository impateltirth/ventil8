# Field data required for final drawings

The repository tooling can size ducts once the following project inputs are
available. Keeping this list explicit prevents illustrative values from being
mistaken for a construction design.

- Dimensioned floor plan, ceiling heights, obstructions, and available shafts
- Process/equipment heat and contaminant sources
- Required local capture points and minimum capture velocities
- Occupancy and outdoor-air requirement
- Applicable building, mechanical, fire, and occupational-safety codes
- Existing supply, exhaust, electrical, and structural constraints
- Make-up air and space-pressure strategy
- Equipment schedules, sound criteria, filtration, and discharge restrictions
- Final diffuser/grille locations and balancing requirements

After collection, populate `design-basis.md`, run the sizing tool for every
segment, reconcile the layer table with the DWG, and export the indexed sheets.
