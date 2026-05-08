"""
PHASE 3 — STEP 4: SEED SUPABASE
Loads all real Janmarg data into database.
Run ONCE only.
"""

import sys, os, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ml.routes_data import ROUTES, ALL_UNIQUE_STOPS
from app.core.config import supabase_admin
from app.core.security import hash_password

def seed_routes():
    print("\nSeeding routes...")
    route_map = {}
    for r in ROUTES:
        result = supabase_admin.table("routes").insert({
            "route_number": r["route_number"],
            "name": r["name"],
            "name_gujarati": r["name_gujarati"],
            "total_stops": len(r["stops"]),
            "distance_km": r["distance_km"],
            "type": r["type"],
            "is_active": True
        }).execute()
        route_map[r["route_number"]] = result.data[0]["id"]
        print(f"  {r['route_number']} — {r['name']}")
    print(f"  Total routes seeded: {len(route_map)}")
    return route_map

def seed_stops(route_map):
    print("\nSeeding stops...")
    stop_map = {}
    for r in ROUTES:
        route_id = route_map[r["route_number"]]
        for seq, stop in enumerate(r["stops"]):
            key = f"{r['route_number']}_{stop['name']}"
            result = supabase_admin.table("stops").insert({
                "name": stop["name"],
                "name_gujarati": stop["name_gujarati"],
                "route_id": route_id,
                "latitude": stop["lat"],
                "longitude": stop["lon"],
                "sequence_number": seq + 1,
                "has_shade": stop["has_shade"],
                "is_metro_connected": stop["is_metro"]
            }).execute()
            stop_map[key] = result.data[0]["id"]
    print(f"  Total stops seeded: {len(stop_map)}")
    return stop_map

def seed_drivers_and_buses(route_map):
    print("\nSeeding drivers and buses...")
    gujarati_names = [
        "Rameshbhai Patel","Sureshbhai Shah","Maheshbhai Modi",
        "Dineshbhai Joshi","Rajeshbhai Desai","Kamleshbhai Trivedi",
        "Bhaveshbhai Mehta","Nileshbhai Gandhi","Alpeshbhai Parmar",
        "Jigneshbhai Solanki","Hareshbhai Chauhan","Nareshbhai Rao",
        "Mukeshbhai Sharma","Prakashbhai Verma","Saileshbhai Nair",
        "Tushar Patel","Vishal Shah","Krunal Modi",
        "Dhruv Joshi","Parth Desai","Meet Trivedi",
        "Jay Mehta","Dev Gandhi","Raj Parmar",
        "Arjun Solanki","Karan Chauhan","Rohan Rao",
        "Sanjay Sharma","Vijay Verma","Anil Kumar",
        "Chirag Patel","Hardik Shah","Neel Modi",
        "Yash Joshi","Rishi Desai","Kush Trivedi"
    ]

    driver_ids = []
    for i, name in enumerate(gujarati_names):
        result = supabase_admin.table("users").insert({
            "email": f"driver{i+1:02d}@chalo.app",
            "hashed_password": hash_password("Driver@1234!"),
            "role": "driver",
            "full_name": name,
            "phone": f"98{''.join([str(random.randint(0,9)) for _ in range(8)])}",
            "language_preference": "gu",
            "is_active": True
        }).execute()
        driver_ids.append(result.data[0]["id"])

    bus_num = 1
    for i, (route_number, route_id) in enumerate(route_map.items()):
        for b in range(2):
            driver_id = driver_ids[(i*2+b) % len(driver_ids)]
            supabase_admin.table("buses").insert({
                "registration_number": f"GJ-01-BRT-{bus_num:03d}",
                "route_id": route_id,
                "driver_id": driver_id,
                "capacity": 60,
                "current_passengers": random.randint(0, 45),
                "status": "active"
            }).execute()
            bus_num += 1

    print(f"  Drivers seeded: {len(gujarati_names)}")
    print(f"  Buses seeded: {bus_num-1}")

def seed_passengers():
    print("\nSeeding sample passengers...")
    for i in range(15):
        supabase_admin.table("users").insert({
            "email": f"passenger{i+1:02d}@test.com",
            "hashed_password": hash_password("Pass@1234!"),
            "role": "passenger",
            "full_name": f"Test Passenger {i+1}",
            "language_preference": "gu" if i % 2 == 0 else "en",
            "is_active": True
        }).execute()
    print("  15 passengers seeded")

def seed_safety_scores(route_map, stop_map):
    print("\nSeeding safety scores...")
    count = 0
    for r in ROUTES:
        route_id = route_map[r["route_number"]]
        for stop in r["stops"]:
            stop_key = f"{r['route_number']}_{stop['name']}"
            stop_id = stop_map.get(stop_key)
            if not stop_id:
                continue
            for hour in range(24):
                time_score = 0.9 if 6 <= hour <= 21 else 0.4
                crowd_score = random.uniform(0.5, 0.95)
                lighting = 0.95 if stop["has_shade"] else 0.65
                overall = (time_score*0.4 + crowd_score*0.3 + lighting*0.3) * 100
                supabase_admin.table("safety_scores").insert({
                    "route_id": route_id,
                    "stop_id": stop_id,
                    "hour_of_day": hour,
                    "day_of_week": 0,
                    "crowding_score": round(crowd_score, 2),
                    "lighting_score": round(lighting, 2),
                    "overall_score": round(overall, 2)
                }).execute()
                count += 1
    print(f"  Safety scores seeded: {count}")

if __name__ == "__main__":
    print("="*50)
    print("CHALO — Seeding Supabase Database")
    print("="*50)
    route_map = seed_routes()
    stop_map = seed_stops(route_map)
    seed_drivers_and_buses(route_map)
    seed_passengers()
    seed_safety_scores(route_map, stop_map)
    print("\n" + "="*50)
    print("Seeding complete!")
    print(f"Routes:   {len(route_map)}")
    print("="*50)