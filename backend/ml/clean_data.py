"""
PHASE 3 — STEP 3: DATA CLEANING
Cleans all three raw datasets.
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def clean_gps():
    print("\nCleaning GPS data...")
    df = pd.read_csv("ml/data/raw/gps_pings_raw.csv")
    original = len(df)

    # Fix timestamps
    def parse_ts(ts):
        for fmt in ["%Y-%m-%dT%H:%M:%S","%Y-%m-%d %H:%M:%S","%d/%m/%y %H:%M","%d/%m/%Y %H:%M"]:
            try: return pd.to_datetime(ts, format=fmt)
            except: continue
        return pd.NaT

    df["timestamp"] = df["timestamp"].apply(parse_ts)
    df = df.dropna(subset=["timestamp"])

    # Remove speed outliers
    df = df[df["speed"] <= 120]

    # Interpolate missing coords
    df = df.sort_values(["bus_id","timestamp"])
    for col in ["latitude","longitude"]:
        df[col] = df.groupby("bus_id")[col].transform(
            lambda x: x.interpolate(method="linear", limit=3)
        )
    df = df.dropna(subset=["latitude","longitude"])
    df = df.drop_duplicates(subset=["bus_id","timestamp"])
    df["latitude"] = df["latitude"].round(5)
    df["longitude"] = df["longitude"].round(5)
    df["speed"] = df["speed"].round(2)

    df.to_csv("ml/data/cleaned/gps_pings_clean.csv", index=False)
    print(f"  {original} → {len(df)} rows (removed {original-len(df)})")

def clean_tickets():
    print("\nCleaning ticket sales...")
    df = pd.read_csv("ml/data/raw/ticket_sales_raw.csv")
    original = len(df)

    df = df.drop_duplicates()
    route_avg = df[df["passenger_count"]>0].groupby("route_number")["passenger_count"].mean()

    def fix_neg(row):
        if row["passenger_count"] < 0:
            return int(route_avg.get(row["route_number"], 20))
        return row["passenger_count"]

    df["passenger_count"] = df.apply(fix_neg, axis=1)
    df["stop_name"] = df["stop_name"].fillna("Unknown Stop")
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"] >= 5
    df["month"] = df["timestamp"].dt.month
    df["date"] = df["timestamp"].dt.date
    df = df[(df["fare"] > 0) & (df["fare"] <= 100)]

    df.to_csv("ml/data/cleaned/ticket_sales_clean.csv", index=False)
    print(f"  {original} → {len(df)} rows (removed {original-len(df)})")

def clean_counts():
    print("\nCleaning passenger counts...")
    df = pd.read_csv("ml/data/raw/passenger_counts_raw.csv")
    df = df[df["passenger_count"] >= 0]
    df["passenger_count"] = df["passenger_count"].clip(0, 300)
    df["date"] = pd.to_datetime(df["date"])
    df.to_csv("ml/data/cleaned/passenger_counts_clean.csv", index=False)
    print(f"  Clean rows: {len(df)}")

def report():
    gps = pd.read_csv("ml/data/cleaned/gps_pings_clean.csv")
    tickets = pd.read_csv("ml/data/cleaned/ticket_sales_clean.csv")
    counts = pd.read_csv("ml/data/cleaned/passenger_counts_clean.csv")

    print("\n" + "="*50)
    print("CLEANING REPORT")
    print("="*50)
    print(f"GPS pings:        {len(gps):,} rows | {gps['bus_id'].nunique()} buses | {gps['route_number'].nunique()} routes")
    print(f"Ticket sales:     {len(tickets):,} rows | {tickets['route_number'].nunique()} routes")
    print(f"Passenger counts: {len(counts):,} rows | {counts['route_number'].nunique()} routes")
    print("="*50)

    summary = {
        "generated_at": datetime.now().isoformat(),
        "gps_clean_rows": len(gps),
        "ticket_clean_rows": len(tickets),
        "count_clean_rows": len(counts),
        "unique_buses": int(gps["bus_id"].nunique()),
        "unique_routes": int(gps["route_number"].nunique())
    }
    import json
    with open("ml/data/cleaned/cleaning_report.json","w") as f:
        json.dump(summary, f, indent=2)

if __name__ == "__main__":
    print("="*50)
    print("CHALO — Cleaning All Data")
    print("="*50)
    clean_gps()
    clean_tickets()
    clean_counts()
    report()