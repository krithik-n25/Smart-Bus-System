"""
PHASE 3 — STEP 2: DATA GENERATION
Generates 6 months of realistic dirty synthetic data
using all 18 real Janmarg BRTS route families.
"""

import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ml.routes_data import ROUTES

def get_demand_multiplier(hour: int, is_weekend: bool, is_festival: bool = False) -> float:
    if is_festival:
        festival_pattern = {
            0:0.3,1:0.2,2:0.2,3:0.2,4:0.3,5:0.5,
            6:0.8,7:1.0,8:1.2,9:1.4,10:1.6,11:1.8,
            12:2.0,13:1.8,14:1.6,15:1.8,16:2.0,17:2.2,
            18:2.5,19:2.8,20:3.0,21:2.5,22:1.8,23:1.0
        }
        return festival_pattern.get(hour, 1.0)
    if is_weekend:
        weekend = {
            0:0.1,1:0.1,2:0.1,3:0.1,4:0.1,5:0.2,
            6:0.4,7:0.5,8:0.6,9:0.7,10:0.8,11:0.9,
            12:1.0,13:0.9,14:0.8,15:0.9,16:1.0,17:1.1,
            18:1.2,19:1.0,20:0.8,21:0.6,22:0.3,23:0.2
        }
        return weekend.get(hour, 0.5)
    weekday = {
        0:0.1,1:0.1,2:0.1,3:0.1,4:0.2,5:0.5,
        6:1.2,7:1.8,8:2.0,9:1.4,
        10:0.8,11:0.7,12:0.9,13:0.8,14:0.7,
        15:0.9,16:1.4,17:1.9,18:2.0,19:1.5,
        20:1.0,21:0.7,22:0.4,23:0.2
    }
    return weekday.get(hour, 0.5)

# Gujarat festival dates (approximate)
FESTIVAL_DATES = [
    "2024-10-13","2024-10-14","2024-10-15",  # Navratri peak
    "2024-01-14","2024-01-15",               # Uttarayan
    "2024-07-07",                             # Rath Yatra
    "2024-11-01","2024-11-02","2024-11-03",  # Diwali
]

def is_festival_day(date: datetime) -> bool:
    return date.strftime("%Y-%m-%d") in FESTIVAL_DATES

def generate_gps_data():
    print("Generating GPS pings...")
    records = []
    start_date = datetime.now() - timedelta(days=180)
    bus_num = 1

    for route in ROUTES:
        # 2 buses per route variant
        for _ in range(2):
            current = start_date
            while current < datetime.now():
                for hour in range(6, 22):
                    for minute in range(0, 60, 3):
                        ts = current.replace(hour=hour, minute=minute, second=0)
                        stop = random.choice(route["stops"])
                        lat = stop["lat"] + random.uniform(-0.001, 0.001)
                        lon = stop["lon"] + random.uniform(-0.001, 0.001)
                        speed = random.uniform(15, 55)

                        # Dirty data
                        if random.random() < 0.05: lat = None
                        if random.random() < 0.05: lon = None
                        if random.random() < 0.02: speed = random.uniform(150, 300)
                        ts_str = ts.strftime("%d/%m/%y %H:%M") if random.random() < 0.03 else ts.isoformat()

                        records.append({
                            "bus_id": f"GJ01BRT{bus_num:03d}",
                            "route_number": route["route_number"],
                            "latitude": lat,
                            "longitude": lon,
                            "speed": speed,
                            "timestamp": ts_str,
                            "is_simulated": True
                        })
                current += timedelta(days=1)
            bus_num += 1

    df = pd.DataFrame(records)
    df.to_csv("ml/data/raw/gps_pings_raw.csv", index=False)
    print(f"  GPS rows generated: {len(df)}")

def generate_ticket_sales():
    print("Generating ticket sales...")
    records = []
    start_date = datetime.now() - timedelta(days=180)

    for route in ROUTES:
        current = start_date
        while current < datetime.now():
            is_weekend = current.weekday() >= 5
            is_fest = is_festival_day(current)
            for stop in route["stops"]:
                for hour in range(6, 22):
                    multiplier = get_demand_multiplier(hour, is_weekend, is_fest)
                    count = int(40 * multiplier * random.uniform(0.7, 1.3))

                    # Dirty data
                    if random.random() < 0.08: count = random.randint(-10, -1)
                    stop_name = None if random.random() < 0.10 else stop["name"]

                    records.append({
                        "route_number": route["route_number"],
                        "stop_name": stop_name,
                        "stop_lat": stop["lat"],
                        "stop_lon": stop["lon"],
                        "timestamp": current.replace(hour=hour, minute=random.randint(0,59)).isoformat(),
                        "passenger_count": count,
                        "ticket_type": random.choice(["single","return","pass"]),
                        "fare": random.choice([5,8,10,12,15]),
                        "is_festival_day": is_fest
                    })
            current += timedelta(days=1)

    df = pd.DataFrame(records)
    # Add 5% duplicates
    df = pd.concat([df, df.sample(frac=0.05)]).reset_index(drop=True)
    df.to_csv("ml/data/raw/ticket_sales_raw.csv", index=False)
    print(f"  Ticket rows generated: {len(df)}")

def generate_passenger_counts():
    print("Generating passenger counts...")
    records = []
    start_date = datetime.now() - timedelta(days=180)

    for route in ROUTES:
        current = start_date
        while current < datetime.now():
            is_weekend = current.weekday() >= 5
            is_fest = is_festival_day(current)
            for stop in route["stops"]:
                for hour in range(0, 24):
                    multiplier = get_demand_multiplier(hour, is_weekend, is_fest)
                    count = int(50 * multiplier * random.uniform(0.8, 1.2))
                    records.append({
                        "route_number": route["route_number"],
                        "stop_name": stop["name"],
                        "hour": hour,
                        "date": current.strftime("%Y-%m-%d"),
                        "day_of_week": current.weekday(),
                        "is_weekend": is_weekend,
                        "is_festival": is_fest,
                        "month": current.month,
                        "passenger_count": max(0, count)
                    })
            current += timedelta(days=1)

    df = pd.DataFrame(records)
    df.to_csv("ml/data/raw/passenger_counts_raw.csv", index=False)
    print(f"  Passenger count rows: {len(df)}")

if __name__ == "__main__":
    print("="*50)
    print("CHALO — Generating Data for ALL 18 BRTS Routes")
    print("="*50)
    generate_gps_data()
    generate_ticket_sales()
    generate_passenger_counts()
    print("="*50)
    print("Done. Check ml/data/raw/")
    print("="*50)