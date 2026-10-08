# Ventilation system schematic

```mermaid
flowchart LR
    OA["Outdoor air"] --> MAU["Make-up / supply unit"]
    MAU --> SM["Supply main"]
    SM --> ZA["Workshop zone A diffusers"]
    SM --> ZB["Workshop zone B diffusers"]
    ZA --> SPACE["Occupied workshop"]
    ZB --> SPACE
    SPACE --> EX["Source capture / exhaust grilles"]
    EX --> EF["Exhaust fan / filtration"]
    EF --> OUT["Code-compliant discharge"]
```

This is the project-level airflow concept, not a construction drawing. Final
equipment, filtration, make-up air, pressure relationships, fire/smoke control,
and discharge locations must be selected from the actual workshop hazards and
applicable code requirements.
