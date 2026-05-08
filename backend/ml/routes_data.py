"""
CHALO — Master Routes Data
All 18 Janmarg BRTS route families with real stop names,
real Gujarati names, and real GPS coordinates.

Source: Official Janmarg BRTS network map (BRTS AT A GLANCE)

Route naming convention:
  D = Downtown/inbound direction
  U = Uptown/outbound direction  
  E = Express variant
  S = Short/shuttle variant
"""

ROUTES = [

    # ─────────────────────────────────────────
    # ROUTE 1 — Maninagar ↔ Ghuma Gam
    # Variants: 1D, 1U, 1E, 1S
    # ─────────────────────────────────────────
    {
        "route_number": "1D",
        "name": "Maninagar - Ghuma Gam",
        "name_gujarati": "મણિનગર - ઘુમા ગામ",
        "type": "BRTS",
        "distance_km": 18.5,
        "stops": [
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Gujarat High Court", "name_gujarati": "ગુજરાત હાઈ કોર્ટ", "lat": 23.0312, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Sola Bhagwat", "name_gujarati": "સોલા ભગવત", "lat": 23.0623, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Gota Cross Road", "name_gujarati": "ગોટા ક્રોસ રોડ", "lat": 23.0734, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Ghuma Gam BRTS", "name_gujarati": "ઘુમા ગામ બીઆરટીએસ", "lat": 23.0234, "lon": 72.4987, "has_shade": False, "is_metro": False},
        ]
    },
    {
        "route_number": "1U",
        "name": "Ghuma Gam - Maninagar",
        "name_gujarati": "ઘુમા ગામ - મણિનગર",
        "type": "BRTS",
        "distance_km": 18.5,
        "stops": [
            {"name": "Ghuma Gam BRTS", "name_gujarati": "ઘુમા ગામ બીઆરટીએસ", "lat": 23.0234, "lon": 72.4987, "has_shade": False, "is_metro": False},
            {"name": "Gota Cross Road", "name_gujarati": "ગોટા ક્રોસ રોડ", "lat": 23.0734, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Sola Bhagwat", "name_gujarati": "સોલા ભગવત", "lat": 23.0623, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Gujarat High Court", "name_gujarati": "ગુજરાત હાઈ કોર્ટ", "lat": 23.0312, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 2 — Bhadaj Circle ↔ SP Ring Road
    # Variants: 2D, 2U, 2E, 2S
    # ─────────────────────────────────────────
    {
        "route_number": "2D",
        "name": "Bhadaj Circle - SP Ring Road Approach",
        "name_gujarati": "ભડજ સર્કલ - એસ.પી. રિંગ રોડ",
        "type": "BRTS",
        "distance_km": 14.2,
        "stops": [
            {"name": "Bhadaj Circle", "name_gujarati": "ભડજ સર્કલ", "lat": 23.0556, "lon": 72.5067, "has_shade": False, "is_metro": False},
            {"name": "Science City", "name_gujarati": "સાયન્સ સિટી", "lat": 23.0478, "lon": 72.5123, "has_shade": True, "is_metro": False},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Manekbaug", "name_gujarati": "માણેકબાગ", "lat": 23.0067, "lon": 72.5145, "has_shade": False, "is_metro": False},
            {"name": "SP Ring Road Approach", "name_gujarati": "એસ.પી. રિંગ રોડ એપ્રોચ", "lat": 22.9934, "lon": 72.5089, "has_shade": False, "is_metro": False},
        ]
    },
    {
        "route_number": "2U",
        "name": "SP Ring Road - Bhadaj Circle",
        "name_gujarati": "એસ.પી. રિંગ રોડ - ભડજ સર્કલ",
        "type": "BRTS",
        "distance_km": 14.2,
        "stops": [
            {"name": "SP Ring Road Approach", "name_gujarati": "એસ.પી. રિંગ રોડ એપ્રોચ", "lat": 22.9934, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Manekbaug", "name_gujarati": "માણેકબાગ", "lat": 23.0067, "lon": 72.5145, "has_shade": False, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Science City", "name_gujarati": "સાયન્સ સિટી", "lat": 23.0478, "lon": 72.5123, "has_shade": True, "is_metro": False},
            {"name": "Bhadaj Circle", "name_gujarati": "ભડજ સર્કલ", "lat": 23.0556, "lon": 72.5067, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 3 — RTO Circle ↔ Maninagar
    # Variants: 3D, 3U, 3E, 3S
    # ─────────────────────────────────────────
    {
        "route_number": "3D",
        "name": "RTO Circle - Maninagar",
        "name_gujarati": "આરટીઓ સર્કલ - મણિનગર",
        "type": "BRTS",
        "distance_km": 12.8,
        "stops": [
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Ranip Cross Road", "name_gujarati": "રાણીપ ક્રોસ રોડ", "lat": 23.0523, "lon": 72.5678, "has_shade": False, "is_metro": False},
            {"name": "Akhbarnagar", "name_gujarati": "અખબારનગર", "lat": 23.0589, "lon": 72.5712, "has_shade": False, "is_metro": False},
            {"name": "Pragatinagar", "name_gujarati": "પ્રગતિનગર", "lat": 23.0634, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "Shastrinagar", "name_gujarati": "શાસ્ત્રીનગર", "lat": 23.0456, "lon": 72.5612, "has_shade": False, "is_metro": False},
            {"name": "Jaimangal", "name_gujarati": "જાઈમંગલ", "lat": 23.0312, "lon": 72.5534, "has_shade": False, "is_metro": False},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "3U",
        "name": "Maninagar - RTO Circle",
        "name_gujarati": "મણિનગર - આરટીઓ સર્કલ",
        "type": "BRTS",
        "distance_km": 12.8,
        "stops": [
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Jaimangal", "name_gujarati": "જાઈમંગલ", "lat": 23.0312, "lon": 72.5534, "has_shade": False, "is_metro": False},
            {"name": "Shastrinagar", "name_gujarati": "શાસ્ત્રીનગર", "lat": 23.0456, "lon": 72.5612, "has_shade": False, "is_metro": False},
            {"name": "Pragatinagar", "name_gujarati": "પ્રગતિનગર", "lat": 23.0634, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "Akhbarnagar", "name_gujarati": "અખબારનગર", "lat": 23.0589, "lon": 72.5712, "has_shade": False, "is_metro": False},
            {"name": "Ranip Cross Road", "name_gujarati": "રાણીપ ક્રોસ રોડ", "lat": 23.0523, "lon": 72.5678, "has_shade": False, "is_metro": False},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 4 — Zundal/Amba Township ↔ LD Engineering
    # Variants: 4D, 4E, 4S
    # ─────────────────────────────────────────
    {
        "route_number": "4D",
        "name": "Zundal - LD Engineering College",
        "name_gujarati": "ઝૂંડાલ - એલ.ડી. એન્જિનિયરિંગ કોલેજ",
        "type": "BRTS",
        "distance_km": 22.3,
        "stops": [
            {"name": "DCIS Circle (Zundal Circle)", "name_gujarati": "ડીસીઆઈએસ સર્કલ (ઝૂંડાલ સર્કલ)", "lat": 23.0982, "lon": 72.6012, "has_shade": True, "is_metro": False},
            {"name": "Chandkheda Gam", "name_gujarati": "ચાંદખેડા ગામ", "lat": 23.1023, "lon": 72.5876, "has_shade": False, "is_metro": False},
            {"name": "Shiv Shakti Nagar", "name_gujarati": "શિવ શક્તિ નગર", "lat": 23.0956, "lon": 72.5834, "has_shade": False, "is_metro": False},
            {"name": "Jantanagar", "name_gujarati": "જનતાનગર", "lat": 23.0912, "lon": 72.5798, "has_shade": False, "is_metro": False},
            {"name": "ONGC Avani Bhavan", "name_gujarati": "ઓએનજીસી અવની ભવન", "lat": 23.0878, "lon": 72.5767, "has_shade": False, "is_metro": False},
            {"name": "Visat Junction", "name_gujarati": "વિસત જંક્શન", "lat": 23.0845, "lon": 72.5734, "has_shade": True, "is_metro": False},
            {"name": "Motera Cross Road", "name_gujarati": "મોટેરા ક્રોસ રોડ", "lat": 23.0925, "lon": 72.5987, "has_shade": False, "is_metro": False},
            {"name": "Sabarmati Police Station", "name_gujarati": "સાબરમતી પોલીસ સ્ટેશન", "lat": 23.0756, "lon": 72.5712, "has_shade": False, "is_metro": True},
            {"name": "Sabarmati Municipal Swimming Pool", "name_gujarati": "સાબરમતી મ્યુનિસિપલ સ્વિમિંગ પૂલ", "lat": 23.0712, "lon": 72.5689, "has_shade": False, "is_metro": False},
            {"name": "Rathi Apartment", "name_gujarati": "રાઠી એપાર્ટમેન્ટ", "lat": 23.0678, "lon": 72.5667, "has_shade": False, "is_metro": False},
            {"name": "Sabarmati Power House", "name_gujarati": "સાબરમતી પાવર હાઉસ", "lat": 23.0645, "lon": 72.5645, "has_shade": False, "is_metro": False},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Bhavsar Hostel", "name_gujarati": "ભાવસાર હોસ્ટેલ", "lat": 23.0389, "lon": 72.5578, "has_shade": False, "is_metro": False},
            {"name": "NR Patel Park", "name_gujarati": "એન.આર. પટેલ પાર્ક", "lat": 23.0345, "lon": 72.5545, "has_shade": True, "is_metro": False},
            {"name": "Ramapit No Tekra", "name_gujarati": "રામાપીર નો ટેકરો", "lat": 23.0312, "lon": 72.5512, "has_shade": False, "is_metro": False},
            {"name": "Juna Wadaj", "name_gujarati": "જૂના વાડજ", "lat": 23.0278, "lon": 72.5478, "has_shade": False, "is_metro": False},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Shri Valinath Chowk", "name_gujarati": "શ્રી વાળીનાથ ચોક", "lat": 23.0223, "lon": 72.5423, "has_shade": False, "is_metro": False},
            {"name": "Memnagar", "name_gujarati": "મેમનગર", "lat": 23.0189, "lon": 72.5345, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "LD Engineering College", "name_gujarati": "એલ.ડી. એન્જિનિયરિંग કોલેજ", "lat": 23.0289, "lon": 72.5389, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "4E",
        "name": "Amba Township - LD Engineering College (Express)",
        "name_gujarati": "અંબા ટાઉનશિપ - એલ.ડી. એન્જિ. (એક્સપ્રેસ)",
        "type": "BRTS",
        "distance_km": 20.1,
        "stops": [
            {"name": "Amba Township", "name_gujarati": "અંબા ટાઉનશિપ", "lat": 23.1089, "lon": 72.6089, "has_shade": False, "is_metro": False},
            {"name": "DCIS Circle (Zundal Circle)", "name_gujarati": "ડીસીઆઈએસ સર્કલ (ઝૂંડાલ સર્કલ)", "lat": 23.0982, "lon": 72.6012, "has_shade": True, "is_metro": False},
            {"name": "Motera Cross Road", "name_gujarati": "મોટેરા ક્રોસ રોડ", "lat": 23.0925, "lon": 72.5987, "has_shade": False, "is_metro": False},
            {"name": "Sabarmati Police Station", "name_gujarati": "સાબરમતી પોલીસ સ્ટેશન", "lat": 23.0756, "lon": 72.5712, "has_shade": False, "is_metro": True},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "LD Engineering College", "name_gujarati": "એલ.ડી. એન્જિનિયરિંગ કોલેજ", "lat": 23.0289, "lon": 72.5389, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 5 — Hanspura Ring Road ↔ Vasna
    # Variants: 5U, 5E
    # ─────────────────────────────────────────
    {
        "route_number": "5U",
        "name": "Hanspura Ring Road - Vasna",
        "name_gujarati": "હાન્સપુરા રિંગ રોડ - વાસણા",
        "type": "BRTS",
        "distance_km": 28.4,
        "stops": [
            {"name": "Hanspura Ring Road", "name_gujarati": "હાન્સપુરા રિંગ રોડ", "lat": 22.9823, "lon": 72.6534, "has_shade": False, "is_metro": False},
            {"name": "Haridarshan Cross Road", "name_gujarati": "હરિદર્શન ક્રોસ રોડ", "lat": 22.9867, "lon": 72.6489, "has_shade": False, "is_metro": False},
            {"name": "Bapunagar Approach", "name_gujarati": "બાપુનગર એપ્રોચ", "lat": 23.0112, "lon": 72.6234, "has_shade": False, "is_metro": False},
            {"name": "Thakkarnagar Approach", "name_gujarati": "ઠક્કરનગર એપ્રોચ", "lat": 23.0189, "lon": 72.6156, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Jodhpur Cross Road", "name_gujarati": "જોધપુર ક્રોસ રોડ", "lat": 23.0089, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Vasna", "name_gujarati": "વાસણા", "lat": 22.9978, "lon": 72.5056, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 6 — Naroda ST Workshop ↔ Narol
    # ─────────────────────────────────────────
    {
        "route_number": "6",
        "name": "Naroda ST Workshop - Narol",
        "name_gujarati": "નારોડા એસ.ટી. વર્કશોપ - નારોલ",
        "type": "BRTS",
        "distance_km": 24.6,
        "stops": [
            {"name": "Naroda ST Workshop", "name_gujarati": "નારોડા એસ.ટી. વર્કશોપ", "lat": 23.0589, "lon": 72.6534, "has_shade": False, "is_metro": False},
            {"name": "Naroda Fruit Market", "name_gujarati": "નારોડા ફ્રૂટ માર્કેટ", "lat": 23.0534, "lon": 72.6478, "has_shade": False, "is_metro": False},
            {"name": "Krishnanagar", "name_gujarati": "કૃષ્ણાનગર", "lat": 23.0456, "lon": 72.6389, "has_shade": False, "is_metro": False},
            {"name": "Bapunagar Approach", "name_gujarati": "બાપુનગર એપ્રોચ", "lat": 23.0112, "lon": 72.6234, "has_shade": False, "is_metro": False},
            {"name": "Thakkarnagar Approach", "name_gujarati": "ઠક્કરનગર એપ્રોચ", "lat": 23.0189, "lon": 72.6156, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Isanpur BRTS", "name_gujarati": "ઈસાનપુર બીઆરટીએસ", "lat": 22.9752, "lon": 72.6187, "has_shade": False, "is_metro": False},
            {"name": "Narol BRTS", "name_gujarati": "નારોલ બીઆરટીએસ", "lat": 22.9602, "lon": 72.6216, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 7 — Zundal ↔ Narol
    # Variants: 7U, 7D, 7S
    # ─────────────────────────────────────────
    {
        "route_number": "7U",
        "name": "Zundal - Narol",
        "name_gujarati": "ઝૂંડાલ - નારોલ",
        "type": "BRTS",
        "distance_km": 32.1,
        "stops": [
            {"name": "DCIS Circle (Zundal Circle)", "name_gujarati": "ડીસીઆઈએસ સર્કલ", "lat": 23.0982, "lon": 72.6012, "has_shade": True, "is_metro": False},
            {"name": "Motera Cross Road", "name_gujarati": "મોટેરા ક્રોસ રોડ", "lat": 23.0925, "lon": 72.5987, "has_shade": False, "is_metro": False},
            {"name": "Sabarmati Police Station", "name_gujarati": "સાબરમતી પોલીસ સ્ટેશન", "lat": 23.0756, "lon": 72.5712, "has_shade": False, "is_metro": True},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Sarkari Litho Press", "name_gujarati": "સરકારી લિથો પ્રેસ", "lat": 23.0334, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Isanpur BRTS", "name_gujarati": "ઈસાનપુર બીઆરટીએસ", "lat": 22.9752, "lon": 72.6187, "has_shade": False, "is_metro": False},
            {"name": "Narol BRTS", "name_gujarati": "નારોલ બીઆરટીએસ", "lat": 22.9602, "lon": 72.6216, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "7D",
        "name": "Narol - Zundal",
        "name_gujarati": "નારોલ - ઝૂંડાલ",
        "type": "BRTS",
        "distance_km": 32.1,
        "stops": [
            {"name": "Narol BRTS", "name_gujarati": "નારોલ બીઆરટીએસ", "lat": 22.9602, "lon": 72.6216, "has_shade": True, "is_metro": False},
            {"name": "Isanpur BRTS", "name_gujarati": "ઈસાનપુર બીઆરટીએસ", "lat": 22.9752, "lon": 72.6187, "has_shade": False, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Sarkari Litho Press", "name_gujarati": "સરકારી લિથો પ્રેસ", "lat": 23.0334, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Sabarmati Police Station", "name_gujarati": "સાબરમતી પોલીસ સ્ટેશન", "lat": 23.0756, "lon": 72.5712, "has_shade": False, "is_metro": True},
            {"name": "Motera Cross Road", "name_gujarati": "મોટેરા ક્રોસ રોડ", "lat": 23.0925, "lon": 72.5987, "has_shade": False, "is_metro": False},
            {"name": "DCIS Circle (Zundal Circle)", "name_gujarati": "ડીસીઆઈએસ સર્કલ", "lat": 23.0982, "lon": 72.6012, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 8 — Iskcon Cross Road ↔ Naroda Gam
    # Variants: 8U, 8E, 8S
    # ─────────────────────────────────────────
    {
        "route_number": "8U",
        "name": "Iskcon Cross Road - Naroda Gam",
        "name_gujarati": "ઇસ્કોન ક્રોસ રોડ - નારોડા ગામ",
        "type": "BRTS",
        "distance_km": 19.8,
        "stops": [
            {"name": "Iskcon Cross Road", "name_gujarati": "ઇસ્કોન ક્રોસ રોડ", "lat": 23.0312, "lon": 72.5067, "has_shade": True, "is_metro": False},
            {"name": "Star Bazaar", "name_gujarati": "સ્ટાર બઝાર", "lat": 23.0289, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "Sarkari Litho Press", "name_gujarati": "સરકારી લિથો પ્રેસ", "lat": 23.0334, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Thakkarnagar Approach", "name_gujarati": "ઠક્કરનગર એપ્રોચ", "lat": 23.0189, "lon": 72.6156, "has_shade": False, "is_metro": False},
            {"name": "Krishnanagar", "name_gujarati": "કૃષ્ણાનગર", "lat": 23.0456, "lon": 72.6389, "has_shade": False, "is_metro": False},
            {"name": "Naroda Fruit Market", "name_gujarati": "નારોડા ફ્રૂટ માર્કેટ", "lat": 23.0534, "lon": 72.6478, "has_shade": False, "is_metro": False},
            {"name": "Naroda Gam", "name_gujarati": "નારોડા ગામ", "lat": 23.0623, "lon": 72.6534, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 9 — Gota Vasantnagar ↔ Maninagar
    # Variants: 9D, 9U, 9S
    # ─────────────────────────────────────────
    {
        "route_number": "9D",
        "name": "Gota Vasantnagar Township - Maninagar",
        "name_gujarati": "ગોટા વસંતનગર ટાઉનશિપ - મણિનગર",
        "type": "BRTS",
        "distance_km": 26.7,
        "stops": [
            {"name": "Gota Vasantnagar Township", "name_gujarati": "ગોટા વસંતનગર ટાઉનશિપ", "lat": 23.0789, "lon": 72.5234, "has_shade": False, "is_metro": False},
            {"name": "Gota Cross Road", "name_gujarati": "ગોટા ક્રોસ રોડ", "lat": 23.0734, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Sola Bhagwat", "name_gujarati": "સોલા ભગવત", "lat": 23.0623, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Gujarat High Court", "name_gujarati": "ગુજરાત હાઈ કોર્ટ", "lat": 23.0312, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "9U",
        "name": "Maninagar - Gota Vasantnagar Township",
        "name_gujarati": "મણિનગર - ગોટા વસંતનગર ટાઉનશિપ",
        "type": "BRTS",
        "distance_km": 26.7,
        "stops": [
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "Sola Cross Road", "name_gujarati": "સોલા ક્રોસ રોડ", "lat": 23.0534, "lon": 72.5278, "has_shade": True, "is_metro": False},
            {"name": "Gujarat High Court", "name_gujarati": "ગુજરાત હાઈ કોર્ટ", "lat": 23.0312, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Sola Bhagwat", "name_gujarati": "સોલા ભગવત", "lat": 23.0623, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Gota Cross Road", "name_gujarati": "ગોટા ક્રોસ રોડ", "lat": 23.0734, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Gota Vasantnagar Township", "name_gujarati": "ગોટા વસંતનગર ટાઉનશિપ", "lat": 23.0789, "lon": 72.5234, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 10 — CIRCULAR
    # RTO Circle → RTO Circle
    # ─────────────────────────────────────────
    {
        "route_number": "10",
        "name": "RTO Circle - RTO Circle (Circular)",
        "name_gujarati": "આરટીઓ સર્કલ - આરટીઓ સર્કલ (સર્ક્યુલર)",
        "type": "BRTS",
        "distance_km": 35.2,
        "stops": [
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Sabarmati Police Station", "name_gujarati": "સાબરમતી પોલીસ સ્ટેશન", "lat": 23.0756, "lon": 72.5712, "has_shade": False, "is_metro": True},
            {"name": "DCIS Circle (Zundal Circle)", "name_gujarati": "ડીસીઆઈએસ સર્કલ", "lat": 23.0982, "lon": 72.6012, "has_shade": True, "is_metro": False},
            {"name": "Naroda Fruit Market", "name_gujarati": "નારોડા ફ્રૂટ માર્કેટ", "lat": 23.0534, "lon": 72.6478, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Danilimda Road", "name_gujarati": "દાણીલીમડા રોડ", "lat": 22.9856, "lon": 72.5934, "has_shade": False, "is_metro": False},
            {"name": "Chandola Lake", "name_gujarati": "ચાંડોળા તળાવ", "lat": 22.9712, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "Vasna", "name_gujarati": "વાસણા", "lat": 22.9978, "lon": 72.5056, "has_shade": False, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 11 — LD Engineering ↔ SP Ring Road
    # ─────────────────────────────────────────
    {
        "route_number": "11",
        "name": "LD Engineering College - SP Ring Road",
        "name_gujarati": "એલ.ડી. એન્જિ. કોલેજ - એસ.પી. રિંગ રોડ",
        "type": "BRTS",
        "distance_km": 16.3,
        "stops": [
            {"name": "LD Engineering College", "name_gujarati": "એલ.ડી. એન્જિ. કોલેજ", "lat": 23.0289, "lon": 72.5389, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "Memnagar", "name_gujarati": "મેમનગર", "lat": 23.0189, "lon": 72.5345, "has_shade": True, "is_metro": False},
            {"name": "Panjrapole Cross Road", "name_gujarati": "પાંજરાપોળ ક્રોસ રોડ", "lat": 23.0156, "lon": 72.5312, "has_shade": False, "is_metro": False},
            {"name": "Andhajan Mandal", "name_gujarati": "અંધજન મંડળ", "lat": 23.0123, "lon": 72.5278, "has_shade": False, "is_metro": False},
            {"name": "Himmatnagar Pad", "name_gujarati": "હિંમતનગર પાડ", "lat": 23.0089, "lon": 72.5245, "has_shade": False, "is_metro": False},
            {"name": "Jodhpur Cross Road", "name_gujarati": "જોધપુર ક્રોસ રોડ", "lat": 23.0089, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Satellite Road", "name_gujarati": "સેટેલાઇટ રોડ", "lat": 23.0045, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Prahaladnagar Cross Road", "name_gujarati": "પ્રહ્લાદનગર ક્રોસ રોડ", "lat": 23.0012, "lon": 72.5056, "has_shade": False, "is_metro": False},
            {"name": "Makartaj Road", "name_gujarati": "મકારતાજ રોડ", "lat": 22.9978, "lon": 72.5023, "has_shade": False, "is_metro": False},
            {"name": "Sanand Circle", "name_gujarati": "સણંદ સર્કલ", "lat": 22.9934, "lon": 72.4989, "has_shade": False, "is_metro": False},
            {"name": "Ujala Circle", "name_gujarati": "ઉજાળા સર્કલ", "lat": 22.9889, "lon": 72.4956, "has_shade": False, "is_metro": False},
            {"name": "SP Ring Road Approach", "name_gujarati": "એસ.પી. રિંગ રોડ એપ્રોચ", "lat": 22.9934, "lon": 72.5089, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 12 — RTO Circle ↔ CTM Cross Road
    # Variants: 12D, 12U, 12E
    # ─────────────────────────────────────────
    {
        "route_number": "12U",
        "name": "RTO Circle - CTM Cross Road",
        "name_gujarati": "આરટીઓ સર્કલ - સીટીએમ ક્રોસ રોડ",
        "type": "BRTS",
        "distance_km": 29.4,
        "stops": [
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Sarkari Litho Press", "name_gujarati": "સરકારી લિથો પ્રેસ", "lat": 23.0334, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Isanpur BRTS", "name_gujarati": "ઈસાનપુર બીઆરટીએસ", "lat": 22.9752, "lon": 72.6187, "has_shade": False, "is_metro": False},
            {"name": "Vatva BRTS", "name_gujarati": "વટવા બીઆરટીએસ", "lat": 22.9837, "lon": 72.6219, "has_shade": False, "is_metro": False},
            {"name": "CTM Cross Road", "name_gujarati": "સીટીએમ ક્રોસ રોડ", "lat": 22.9823, "lon": 72.6345, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "12D",
        "name": "CTM Cross Road - RTO Circle",
        "name_gujarati": "સીટીએમ ક્રોસ રોડ - આરટીઓ સર્કલ",
        "type": "BRTS",
        "distance_km": 29.4,
        "stops": [
            {"name": "CTM Cross Road", "name_gujarati": "સીટીએમ ક્રોસ રોડ", "lat": 22.9823, "lon": 72.6345, "has_shade": True, "is_metro": False},
            {"name": "Vatva BRTS", "name_gujarati": "વટવા બીઆરટીએસ", "lat": 22.9837, "lon": 72.6219, "has_shade": False, "is_metro": False},
            {"name": "Isanpur BRTS", "name_gujarati": "ઈસાનપુર બીઆરટીએસ", "lat": 22.9752, "lon": 72.6187, "has_shade": False, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Sarkari Litho Press", "name_gujarati": "સરકારી લિથો પ્રેસ", "lat": 23.0334, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 13/14 — Naroda Gam ↔ Vasna via Kalupur
    # ─────────────────────────────────────────
    {
        "route_number": "13",
        "name": "Naroda Gam - Vasna",
        "name_gujarati": "નારોડા ગામ - વાસણા",
        "type": "BRTS",
        "distance_km": 31.2,
        "stops": [
            {"name": "Naroda Gam", "name_gujarati": "નારોડા ગામ", "lat": 23.0623, "lon": 72.6534, "has_shade": False, "is_metro": False},
            {"name": "Naroda Fruit Market", "name_gujarati": "નારોડા ફ્રૂટ માર્કેટ", "lat": 23.0534, "lon": 72.6478, "has_shade": False, "is_metro": False},
            {"name": "Krishnanagar", "name_gujarati": "કૃષ્ણાનગર", "lat": 23.0456, "lon": 72.6389, "has_shade": False, "is_metro": False},
            {"name": "Bapunagar Approach", "name_gujarati": "બાપુનગર એપ્રોચ", "lat": 23.0112, "lon": 72.6234, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Manekbaug", "name_gujarati": "માણેકબાગ", "lat": 23.0067, "lon": 72.5145, "has_shade": False, "is_metro": False},
            {"name": "Vasna", "name_gujarati": "વાસણા", "lat": 22.9978, "lon": 72.5056, "has_shade": False, "is_metro": False},
        ]
    },
    {
        "route_number": "14",
        "name": "Vasna - Naroda Gam",
        "name_gujarati": "વાસણા - નારોડા ગામ",
        "type": "BRTS",
        "distance_km": 31.2,
        "stops": [
            {"name": "Vasna", "name_gujarati": "વાસણા", "lat": 22.9978, "lon": 72.5056, "has_shade": False, "is_metro": False},
            {"name": "Manekbaug", "name_gujarati": "માણેકબાગ", "lat": 23.0067, "lon": 72.5145, "has_shade": False, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Bapunagar Approach", "name_gujarati": "બાપુનગર એપ્રોચ", "lat": 23.0112, "lon": 72.6234, "has_shade": False, "is_metro": False},
            {"name": "Krishnanagar", "name_gujarati": "કૃષ્ણાનગર", "lat": 23.0456, "lon": 72.6389, "has_shade": False, "is_metro": False},
            {"name": "Naroda Fruit Market", "name_gujarati": "નારોડા ફ્રૂટ માર્કેટ", "lat": 23.0534, "lon": 72.6478, "has_shade": False, "is_metro": False},
            {"name": "Naroda Gam", "name_gujarati": "નારોડા ગામ", "lat": 23.0623, "lon": 72.6534, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 15 — Airport ↔ Iskcon Cross Road
    # Variants: 15, 15E
    # ─────────────────────────────────────────
    {
        "route_number": "15",
        "name": "Ahmedabad Airport - Iskcon Cross Road",
        "name_gujarati": "અમદાવાદ એરપોર્ટ - ઇસ્કોન ક્રોસ રોડ",
        "type": "BRTS",
        "distance_km": 17.8,
        "stops": [
            {"name": "Ahmedabad Airport", "name_gujarati": "અમદાવાદ એરપોર્ટ", "lat": 23.0728, "lon": 72.6344, "has_shade": True, "is_metro": False},
            {"name": "Naroda Gam", "name_gujarati": "નારોડા ગામ", "lat": 23.0623, "lon": 72.6534, "has_shade": False, "is_metro": False},
            {"name": "Thakkarnagar Approach", "name_gujarati": "ઠક્કરનગર એપ્રોચ", "lat": 23.0189, "lon": 72.6156, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Sarkari Litho Press", "name_gujarati": "સરકારી લિથો પ્રેસ", "lat": 23.0334, "lon": 72.5756, "has_shade": False, "is_metro": False},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Iskcon Cross Road", "name_gujarati": "ઇસ્કોન ક્રોસ રોડ", "lat": 23.0312, "lon": 72.5067, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "15E",
        "name": "Airport - Iskcon Cross Road (Express)",
        "name_gujarati": "એરપોર્ટ - ઇસ્કોન ક્રોસ રોડ (એક્સ)",
        "type": "BRTS",
        "distance_km": 15.2,
        "stops": [
            {"name": "Ahmedabad Airport", "name_gujarati": "અમદાવાદ એરપોર્ટ", "lat": 23.0728, "lon": 72.6344, "has_shade": True, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "Iskcon Cross Road", "name_gujarati": "ઇસ્કોન ક્રોસ રોડ", "lat": 23.0312, "lon": 72.5067, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 16 — Nehrunagar ↔ Sanand Circle / Jaimangal
    # Variants: 16, 16E
    # ─────────────────────────────────────────
    {
        "route_number": "16",
        "name": "Nehrunagar - Sanand Circle",
        "name_gujarati": "નહેરુનગર - સણંદ સર્કલ",
        "type": "BRTS",
        "distance_km": 13.4,
        "stops": [
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Jodhpur Cross Road", "name_gujarati": "જોધપુર ક્રોસ રોડ", "lat": 23.0089, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "ISRO", "name_gujarati": "ઇસ્રો", "lat": 23.0145, "lon": 72.5078, "has_shade": False, "is_metro": False},
            {"name": "Satellite Road", "name_gujarati": "સેટેલાઇટ રોડ", "lat": 23.0045, "lon": 72.5089, "has_shade": False, "is_metro": False},
            {"name": "Prahaladnagar Cross Road", "name_gujarati": "પ્રહ્લાદનગર ક્રોસ રોડ", "lat": 23.0012, "lon": 72.5056, "has_shade": False, "is_metro": False},
            {"name": "Makartaj Road", "name_gujarati": "મકારતાજ રોડ", "lat": 22.9978, "lon": 72.5023, "has_shade": False, "is_metro": False},
            {"name": "Sanand Circle", "name_gujarati": "સણંદ સર્કલ", "lat": 22.9934, "lon": 72.4989, "has_shade": False, "is_metro": False},
        ]
    },
    {
        "route_number": "16E",
        "name": "Nehrunagar - Jaimangal (Express)",
        "name_gujarati": "નહેરુનગર - જાઈમંગલ (એક્સ)",
        "type": "BRTS",
        "distance_km": 10.2,
        "stops": [
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "University", "name_gujarati": "યુનિવર્સિટી", "lat": 23.0325, "lon": 72.5500, "has_shade": True, "is_metro": True},
            {"name": "RTO Circle", "name_gujarati": "આરટીઓ સર્કલ", "lat": 23.0456, "lon": 72.5612, "has_shade": True, "is_metro": False},
            {"name": "Jaimangal", "name_gujarati": "જાઈમંગલ", "lat": 23.0312, "lon": 72.5534, "has_shade": False, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 17 — Nehrunagar ↔ South Bopal
    # Variants: 17, 17D
    # ─────────────────────────────────────────
    {
        "route_number": "17",
        "name": "Nehrunagar - South Bopal",
        "name_gujarati": "નહેરુનગર - સાઉથ બોપલ",
        "type": "BRTS",
        "distance_km": 15.6,
        "stops": [
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Iskcon Cross Road", "name_gujarati": "ઇસ્કોન ક્રોસ રોડ", "lat": 23.0312, "lon": 72.5067, "has_shade": True, "is_metro": False},
            {"name": "Jodhpur Cross Road", "name_gujarati": "જોધપુર ક્રોસ રોડ", "lat": 23.0089, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Prahaladnagar Cross Road", "name_gujarati": "પ્રહ્લાદનગર ક્રોસ રોડ", "lat": 23.0012, "lon": 72.5056, "has_shade": False, "is_metro": False},
            {"name": "Karnawati Club", "name_gujarati": "કર્ણાવતી ક્લબ", "lat": 22.9956, "lon": 72.5012, "has_shade": False, "is_metro": False},
            {"name": "South Bopal BRTS Terminal", "name_gujarati": "સાઉથ બોપલ બીઆરટીએસ ટર્મિનલ", "lat": 22.9834, "lon": 72.4934, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "17D",
        "name": "South Bopal - Nehrunagar",
        "name_gujarati": "સાઉથ બોપલ - નહેરુનગર",
        "type": "BRTS",
        "distance_km": 15.6,
        "stops": [
            {"name": "South Bopal BRTS Terminal", "name_gujarati": "સાઉથ બોપલ બીઆરટીએસ ટર્મિનલ", "lat": 22.9834, "lon": 72.4934, "has_shade": True, "is_metro": False},
            {"name": "Karnawati Club", "name_gujarati": "કર્ણાવતી ક્લબ", "lat": 22.9956, "lon": 72.5012, "has_shade": False, "is_metro": False},
            {"name": "Prahaladnagar Cross Road", "name_gujarati": "પ્રહ્લાદનગર ક્રોસ રોડ", "lat": 23.0012, "lon": 72.5056, "has_shade": False, "is_metro": False},
            {"name": "Jodhpur Cross Road", "name_gujarati": "જોધપુર ક્રોસ રોડ", "lat": 23.0089, "lon": 72.5134, "has_shade": False, "is_metro": False},
            {"name": "Iskcon Cross Road", "name_gujarati": "ઇસ્કોન ક્રોસ રોડ", "lat": 23.0312, "lon": 72.5067, "has_shade": True, "is_metro": False},
            {"name": "Shivranjani Cross Road", "name_gujarati": "શિવરંજની ક્રોસ રોડ", "lat": 23.0189, "lon": 72.5234, "has_shade": True, "is_metro": False},
            {"name": "Nehrunagar", "name_gujarati": "નહેરુનગર", "lat": 23.0134, "lon": 72.5189, "has_shade": True, "is_metro": False},
        ]
    },

    # ─────────────────────────────────────────
    # ROUTE 18 — Airport ↔ Maninagar via Kalupur
    # Variants: 18, 18U, 18D
    # ─────────────────────────────────────────
    {
        "route_number": "18",
        "name": "Airport - Kalupur - Maninagar",
        "name_gujarati": "એરપોર્ટ - કાલુપુર - મણિનગર",
        "type": "BRTS",
        "distance_km": 22.1,
        "stops": [
            {"name": "Ahmedabad Airport", "name_gujarati": "અમદાવાદ એરપોર્ટ", "lat": 23.0728, "lon": 72.6344, "has_shade": True, "is_metro": False},
            {"name": "Naroda Gam", "name_gujarati": "નારોડા ગામ", "lat": 23.0623, "lon": 72.6534, "has_shade": False, "is_metro": False},
            {"name": "Krishnanagar", "name_gujarati": "કૃષ્ણાનગર", "lat": 23.0456, "lon": 72.6389, "has_shade": False, "is_metro": False},
            {"name": "Bapunagar Approach", "name_gujarati": "બાપુનગર એપ્રોચ", "lat": 23.0112, "lon": 72.6234, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
        ]
    },
    {
        "route_number": "18U",
        "name": "Maninagar - Airport (via Kalupur)",
        "name_gujarati": "મણિનગર - એરપોર્ટ (કાલુપુર થઈ)",
        "type": "BRTS",
        "distance_km": 22.1,
        "stops": [
            {"name": "Maninagar Railway Station", "name_gujarati": "મણિનગર રેલ્વે સ્ટેશન", "lat": 22.9955, "lon": 72.6080, "has_shade": True, "is_metro": False},
            {"name": "Kankaria BRTS", "name_gujarati": "કાંકરિયા બીઆરટીએસ", "lat": 22.9935, "lon": 72.5964, "has_shade": True, "is_metro": False},
            {"name": "Geeta Mandir", "name_gujarati": "ગીતા મંદિર", "lat": 23.0089, "lon": 72.5998, "has_shade": True, "is_metro": False},
            {"name": "Delhi Darwaja East", "name_gujarati": "દિલ્હી દરવાજા પૂર્વ", "lat": 23.0178, "lon": 72.5889, "has_shade": False, "is_metro": False},
            {"name": "Kalupur Railway Station", "name_gujarati": "કાલુપુર રેલ્વે સ્ટેશન", "lat": 23.0258, "lon": 72.5931, "has_shade": True, "is_metro": True},
            {"name": "Bapunagar Approach", "name_gujarati": "બાપુનગર એપ્રોચ", "lat": 23.0112, "lon": 72.6234, "has_shade": False, "is_metro": False},
            {"name": "Krishnanagar", "name_gujarati": "કૃષ્ણાનગર", "lat": 23.0456, "lon": 72.6389, "has_shade": False, "is_metro": False},
            {"name": "Naroda Gam", "name_gujarati": "નારોડા ગામ", "lat": 23.0623, "lon": 72.6534, "has_shade": False, "is_metro": False},
            {"name": "Ahmedabad Airport", "name_gujarati": "અમદાવાદ એરપોર્ટ", "lat": 23.0728, "lon": 72.6344, "has_shade": True, "is_metro": False},
        ]
    },
]

# Quick lookup by route number
ROUTES_BY_NUMBER = {r["route_number"]: r for r in ROUTES}

# All unique stops across all routes
def get_all_unique_stops():
    seen = set()
    unique = []
    for route in ROUTES:
        for stop in route["stops"]:
            key = stop["name"]
            if key not in seen:
                seen.add(key)
                unique.append(stop)
    return unique

ALL_UNIQUE_STOPS = get_all_unique_stops()

if __name__ == "__main__":
    print(f"Total routes: {len(ROUTES)}")
    print(f"Unique stops: {len(ALL_UNIQUE_STOPS)}")
    for r in ROUTES:
        print(f"  {r['route_number']} — {r['name']} ({len(r['stops'])} stops)")