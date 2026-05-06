"""
Average daily temperatures in Redmond, WA — Jan 1 through Apr 21
─────────────────────────────────────────────────────────────────
Source: Climatological normals (MERRA-2 / historical station data).
Values are daily mean °F, computed as (avg_high + avg_low) / 2 per
the historical monthly profiles from wanderlog/weather-us/weatherspark.

Monthly reference points used:
  Jan : high 43°F, low 33°F  → mean ~38°F  (slight warming trend through month)
  Feb : high 44°F, low 33°F  → mean ~38.5°F
  Mar : high 49°F, low 36°F  → mean ~42.5°F  (spring warming begins)
  Apr : high 55°F, low 40°F  → mean ~47.5°F  (57→63°F high range; linear interp)

Daily values are linearly interpolated across each month's warming gradient.
These are climate normals, not observed 2026 actuals.
"""

from datetime import date, timedelta

# Monthly (avg_high, avg_low) in °F — climatological normals
monthly_params = {
    1: (43.0, 33.0),   # January
    2: (44.0, 33.0),   # February
    3: (49.0, 36.0),   # March
    4: (57.0, 40.0),   # April (mid-month ref; starts ~55, ends ~63)
}

def daily_mean(month: int, day: int) -> float:
    """Linearly interpolate daily mean temp within a month."""
    import calendar
    days_in_month = calendar.monthrange(2026, month)[1]

    # Blend current month toward next month's values
    if month < 4:
        next_month = month + 1
    else:
        next_month = month  # For April, just use April values (no blending needed)

    h_start, l_start = monthly_params[month]
    h_end, l_end = monthly_params[next_month]

    frac = (day - 1) / days_in_month
    h = h_start + frac * (h_end - h_start)
    l = l_start + frac * (l_end - l_start)
    return round((h + l) / 2, 1)


# Build the dictionary: {"YYYY-MM-DD": avg_temp_F}
start = date(2026, 1, 1)
end   = date(2026, 4, 21)

redmond_avg_temp_f: dict[str, float] = {}

current = start
while current <= end:
    temp = daily_mean(current.month, current.day)
    redmond_avg_temp_f[current.isoformat()] = temp
    current += timedelta(days=1)


# ── Quick sanity check ──────────────────────────────────────────
if __name__ == "__main__":
    print(f"Entries: {len(redmond_avg_temp_f)}")
    for date_str, temp in list(redmond_avg_temp_f.items())[::15]:  # every 15 days
        print(f"  {date_str}: {temp}°F")

print(redmond_avg_temp_f)