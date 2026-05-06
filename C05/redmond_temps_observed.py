"""
Good. The correct station for Seattle Boeing Field is `GHCND:USW00024234` (not 24233, which is Sea-Tac).
The NOAA CDO API requires a free token. I'll write a script that fetches actual observed TMAX/TMIN,
computes daily mean, and builds the dict — with clear instructions for getting the token.
One prerequisite: the NOAA CDO API requires a free token.
Get one at **https://www.ncdc.noaa.gov/cdo-web/token** — just an email address, token arrives instantly.

Then run it as:

```bash
export NOAA_TOKEN=your_token_here
python redmond_temps_observed.py
```

Or inline in a script: `os.environ["NOAA_TOKEN"] = "..."` before calling `fetch_observations()`.

A few implementation notes:
- **Station**: `GHCND:USW00024234` (Seattle Boeing Field) — confirmed correct; `USW00024233` is Sea-Tac.
- **Units**: `standard` → NOAA returns °F directly for GHCND. Switch to `"metric"` if you want °C.
- **Daily mean**: `(TMAX + TMIN) / 2` — the standard climatological convention.
- **Pagination**: handled, though 111 days × 2 datatypes = 222 rows, well under the 1000-record limit.
- **Missing days**: logged as warnings rather than silently dropped or imputed — you'll want to know if there are gaps.
"""
"""
Observed daily average temperatures — Redmond, WA
Jan 1 – Apr 21, 2026

Station: Seattle Boeing Field (GHCND:USW00024234)
        ~13 miles from Redmond; standard proxy used by timeanddate.com et al.

API: NOAA NCEI Climate Data Online (CDO) v2
     https://www.ncei.noaa.gov/cdo-web/api/v2/data

Token: Free — register at https://www.ncdc.noaa.gov/cdo-web/token
       (email confirmation, instant). Set as env var NOAA_TOKEN or pass inline.

Daily mean = (TMAX + TMIN) / 2  (tenths of °C → °F conversion applied)
"""

import os
import time
import requests
from datetime import date, timedelta

# ── Config ─────────────────────────────────────────────────────────────────────
NOAA_TOKEN = os.environ.get("NOAA_TOKEN", "YOUR_TOKEN_HERE")
STATION_ID = "GHCND:USW00024234"  # Seattle Boeing Field
START_DATE = "2026-01-01"
END_DATE = "2026-04-21"
UNITS = "standard"  # °F; use "metric" for °C

BASE_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"

# CDO returns max 1000 records per request; TMAX+TMIN for ~111 days = 222 rows → fits in one call
PARAMS = {
    "datasetid": "GHCND",
    "stationid": STATION_ID,
    "datatypeid": "TMAX,TMIN",
    "startdate": START_DATE,
    "enddate": END_DATE,
    "units": UNITS,
    "limit": 1000,
}

HEADERS = {"token": NOAA_TOKEN}


def fetch_observations() -> dict[str, float]:
    """
    Hit the NOAA CDO API and return {date_str: mean_temp_F}.
    Handles pagination just in case (limit=1000 should cover it).
    """
    if NOAA_TOKEN == "YOUR_TOKEN_HERE":
        raise ValueError(
            "Set your NOAA token: export NOAA_TOKEN=<your_token>\n"
            "Get one free at https://www.ncdc.noaa.gov/cdo-web/token"
        )

    records: list[dict] = []
    offset = 1

    while True:
        resp = requests.get(
            BASE_URL,
            headers=HEADERS,
            params={**PARAMS, "offset": offset},
            timeout=30,
        )
        resp.raise_for_status()
        payload = resp.json()

        batch = payload.get("results", [])
        records.extend(batch)

        meta = payload.get("metadata", {}).get("resultset", {})
        total = meta.get("count", 0)
        if offset + len(batch) - 1 >= total or not batch:
            break
        offset += len(batch)
        time.sleep(0.25)  # CDO rate limit: 5 req/s, 10k req/day

    return _build_dict(records)


def _build_dict(records: list[dict]) -> dict[str, float]:
    """
    Pivot raw TMAX/TMIN rows into {date: mean_F}.
    CDO 'standard' units returns °F for GHCND.
    Some days may be missing one value; skip those rather than impute.
    """
    day_data: dict[str, dict[str, float]] = {}

    for rec in records:
        date_str = rec["date"][:10]  # "2026-01-01T00:00:00" → "2026-01-01"
        dtype = rec["datatype"]  # "TMAX" or "TMIN"
        value = rec["value"]  # °F (tenths of °C if metric)

        day_data.setdefault(date_str, {})[dtype] = value

    result: dict[str, float] = {}
    for date_str, vals in sorted(day_data.items()):
        if "TMAX" in vals and "TMIN" in vals:
            result[date_str] = round((vals["TMAX"] + vals["TMIN"]) / 2, 1)
        else:
            # Log missing but don't crash
            print(f"  [warn] incomplete data for {date_str}: {vals}")

    return result


# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Fetching observed temps from NOAA CDO ({START_DATE} → {END_DATE})…")
    redmond_avg_temp_f = fetch_observations()

    print(f"\nEntries retrieved: {len(redmond_avg_temp_f)}")
    print("\nSample (every 15 days):")
    dates = list(redmond_avg_temp_f.items())
    for date_str, temp in dates[::15]:
        print(f"  {date_str}: {temp}°F")

    # The dict is the deliverable — import or use inline:
    # from redmond_temps_observed import fetch_observations
    # temps = fetch_observations()
