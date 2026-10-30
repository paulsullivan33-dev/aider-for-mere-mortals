"""A tiny garden planner used as this guide's practice project.

It answers two questions for a small vegetable bed:
how long until a crop can be picked, and how much
water the bed needs on a dry day.
"""

CROPS = {
    "tomato": {"days": 80, "water_per_plant": 1.5},
    "lettuce": {"days": 45, "water_per_plant": 0.5},
    "carrot": {"days": 70, "water_per_plant": 0.4},
    "bean": {"days": 55, "water_per_plant": 0.8},
}


def days_to_harvest(crop, days_since_sowing):
    """Days left before `crop` is ready, never below zero."""
    total = CROPS[crop]["days"]
    return max(0, total - days_since_sowing)


def water_litres(plants):
    """Total litres for one watering.

    `plants` is a dict of crop name to plant count,
    for example {"tomato": 4, "lettuce": 10}.
    """
    total = 0.0
    for crop, count in plants.items():
        total += CROPS[crop]["water_per_plant"] * count
    return round(total, 2)


def bed_summary(plants, days_since_sowing):
    """One-line summary for each crop in the bed."""
    lines = []
    for crop in sorted(plants):
        left = days_to_harvest(crop, days_since_sowing)
        lines.append(f"{crop}: {left} days to harvest")
    return lines
