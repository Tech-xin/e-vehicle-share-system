# insert_data.py

from customer.models import Vehicle
from datetime import time

'''# Dictionary with cities, places, prices, and operating hours for each place
cities_and_places = {
    "Aberdeen": {
        "Union Street": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(22, 0)},
        "Marischal College": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Aberdeen Beach": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(23, 0)},
        "Duthie Park": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
    },
    "Birmingham": {
        "Bullring & Grand Central": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Jewellery Quarter": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
        "The Mailbox": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(21, 0)},
        "Digbeth": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
    },
    "Brighton": {
        "Brighton Pier": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(22, 0)},
        "The Lanes": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Brighton Marina": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(23, 0)},
        "Hove": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
    },
    "Cambridge": {
        "Central": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Station": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Botanic Garden": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "River Cam": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(22, 0)},
    },
    "Dundee": {
        "City Centre": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "V&A Dundee": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(22, 0)},
        "Discovery Point": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Broughty Ferry": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
    "Edinburgh": {
        "Princes Street": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Royal Mile": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Leith": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Edinburgh Castle": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
    "Glasgow": {
        "Buchanan Street": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Byres Road": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(21, 0)},
        "George Square": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Merchant City": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(23, 0)},
        "University of Glasgow": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
    "Leeds": {
        "Leeds Dock": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Roundhay Park": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Briggate": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Millennium Square": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
    "Liverpool": {
        "Albert Dock": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Anfield": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Sefton Park": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Liverpool ONE": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
    "London": {
        "Central": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Westminster": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
        "Camden": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(21, 0)},
        "Covent Garden": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
    },
    "Manchester": {
        "Deansgate": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Northern Quarter": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Salford Quays": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(20, 0)},
        "Piccadilly": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(21, 0)},
    },
    "Newcatle": {
        "Quayside": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(21, 0)},
        "Grey Street": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Newcastle University": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(20, 0)},
        "Eldon Square": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(23, 0)},
    },
    "Nottingham": {
        "Old Market Square": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Wollaton Park": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Lace Market": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Nottingham Castle": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
    "Oxford": {
        "Oxford Center": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Headington": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Cowley Road": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(20, 0)},
        "Summertown": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(21, 0)},
    },
    "Sheffield": {
        "Peace Gardens": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(21, 0)},
        "Meadowhall": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(8, 0), "closing": time(22, 0)},
        "Sheffield University": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(6, 0), "closing": time(20, 0)},
        "Kelham Island": {"price_bike": 0.40, "price_scooter": 0.30, "opening": time(7, 0), "closing": time(23, 0)},
    },
}'''

# Dictionary with cities, places, and their latitude and longitude coordinates
cities_and_places = {
    "Aberdeen": {
        "Union Street": {"latitude": 57.1475, "longitude": -2.0954},
        "Marischal College": {"latitude": 57.1496, "longitude": -2.0962},
        "Aberdeen Beach": {"latitude": 57.1526, "longitude": -2.0825},
        "Duthie Park": {"latitude": 57.1310, "longitude": -2.1040},
    },
    "Birmingham": {
        "Bullring & Grand Central": {"latitude": 52.4776, "longitude": -1.8945},
        "Jewellery Quarter": {"latitude": 52.4894, "longitude": -1.9132},
        "The Mailbox": {"latitude": 52.4763, "longitude": -1.9052},
        "Digbeth": {"latitude":52.4740, "longitude":-1.8860},
    },
    "Brighton": {
        "Brighton Pier": {"latitude":50.8167, "longitude":-0.1372},
        "The Lanes": {"latitude":50.8225, "longitude":-0.1427},
        "Brighton Marina": {"latitude":50.8128, "longitude":-0.1039},
        "Hove": {"latitude":50.8303, "longitude":-0.1674},
    },
    "Cambridge": {
        "Central": {"latitude":52.2053, "longitude":0.1218},
        "Station": {"latitude":52.1944, "longitude":0.1375},
        "Botanic Garden": {"latitude":52.1970, "longitude":0.1234},
        "River Cam": {"latitude":52.2113, "longitude":0.1174},
    },
    "Dundee": {
        "City Centre": {"latitude":56.4620, "longitude":-2.9707},
        "V&A Dundee": {"latitude":56.4597, "longitude":-2.9595},
        "Discovery Point": {"latitude":56.4590,"longitude": -2.9677},
        "Broughty Ferry": {"latitude":56.4676,"longitude": -2.8735},
    },
    "Edinburgh": {
        "Princes Street": {"latitude":55.9520,"longitude": -3.1965},
        "Royal Mile": {"latitude":55.9500, "longitude":-3.1875},
        "Leith": {"latitude":55.9710,"longitude": -3.1692},
        "Edinburgh Castle": {"latitude":55.9486,"longitude": -3.1999},
    },
    "Glasgow": {
        "Buchanan Street": {"latitude":55.8620,"longitude": -4.2520},
        "Byres Road": {"latitude":55.8750, "longitude":-4.2930},
        "George Square": {"latitude":55.8610,"longitude": -4.2500},
        "Merchant City": {"latitude":55.8580, "longitude":-4.2470},
        "University of Glasgow": {"latitude":55.8721,"longitude": -4.2886},
    },
    "Leeds": {
        "Leeds Dock": {"latitude":53.7915,"longitude": -1.5282},
        "Roundhay Park": {"latitude":53.8458, "longitude":-1.5014},
        "Briggate": {"latitude":53.7966,"longitude": -1.5417},
        "Millennium Square": {"latitude":53.8008,"longitude": -1.5491},
    },
    "Liverpool": {
        "Albert Dock": {"latitude":53.3997,"longitude": -2.9916},
        "Anfield": {"latitude":53.4308,"longitude": -2.9608},
        "Sefton Park": {"latitude":53.3834, "longitude":-2.9367},
        "Liverpool ONE": {"latitude":53.4036,"longitude": -2.9847},
    },
    "London": {
        "Central": {"latitude":51.5098,"longitude": -0.1180},
        "Westminster": {"latitude":51.4975, "longitude":-0.1357},
        "Camden": {"latitude":51.5415,"longitude": -0.1432},
        "Covent Garden": {"latitude":51.5114,"longitude": -0.1240},
    },
    "Manchester": {
        "Deansgate": {"latitude":53.4773,"longitude": -2.2514},
        "Northern Quarter": {"latitude":53.4842,"longitude": -2.2362},
        "Salford Quays": {"latitude":53.4691, "longitude":-2.2988},
        "Piccadilly": {"latitude":53.4818,"longitude": -2.2324},
    },
    "Newcastle": {
        "Quayside": {"latitude":54.9681,"longitude": -1.6066},
        "Grey Street": {"latitude":54.9737,"longitude": -1.6135},
        "Newcastle University": {"latitude":54.9783,"longitude": -1.6174},
        "Eldon Square": {"latitude":54.9730,"longitude": -1.6175},
    },
    "Nottingham": {
        "Old Market Square": {"latitude":52.9536,"longitude": -1.1505},
        "Wollaton Park": {"latitude":52.9471,"longitude": -1.2182},
        "Lace Market": {"latitude":52.9546,"longitude": -1.1444},
        "Nottingham Castle": {"latitude":52.9507,"longitude": -1.1542},
    },
    "Oxford": {
        "Oxford Center": {"latitude":51.7548,"longitude": -1.2544},
        "Headington": {"latitude":51.7594,"longitude": -1.2122},
        "Cowley Road": {"latitude":51.7437,"longitude": -1.2321},
        "Summertown": {"latitude":51.7841,"longitude": -1.2635},
    },
    "Sheffield": {
        "Peace Gardens": {"latitude":53.3808,"longitude": -1.4705},
        "Meadowhall": {"latitude":53.4143,"longitude": -1.4122},
        "Sheffield University": {"latitude":53.3811,"longitude": -1.4873},
        "Kelham Island": {"latitude":53.3890,"longitude": -1.4725},
    },
}

# Loop through the cities and places, updating latitude and longitude for existing records
for city, places in cities_and_places.items():
    for place, coordinates in places.items():
        # Find all vehicles in the given city and place
        vehicles = Vehicle.objects.filter(city_name=city, place_name=place)
        
        # Update latitude and longitude for each vehicle found
        for vehicle in vehicles:
            vehicle.location_lati = coordinates['latitude']
            vehicle.location_longi = coordinates['longitude']
            vehicle.save()
            print(f"Updated {vehicle.city_name} - {vehicle.place_name} with lat: {vehicle.location_lati}, long: {vehicle.location_longi}")

print("Latitude and longitude updated for all specified locations.")

'''
# Remove existing entries to start with a clean slate
#Vehicle.objects.all().delete()

vehicles = []
for city, places in cities_and_places.items():
    for place, details in places.items():
        # Add 5 bikes for each place
        for i in range(5):
            vehicles.append(Vehicle(
                type='bike',
                city_name=city,
                place_name=place,
                price_per_minute=details['price_bike'],
                day_pass=7.99,
                monthly_subscription=28.99,
                annual_subscription=149.99,
                opening_time=details['opening'],
                closing_time=details['closing']
            ))

        # Add 5 scooters for each place
        for i in range(5):
            vehicles.append(Vehicle(
                type='scooter',
                city_name=city,
                place_name=place,
                price_per_minute=details['price_scooter'],
                day_pass=7.99,
                monthly_subscription=28.99,
                annual_subscription=149.99,
                opening_time=details['opening'],
                closing_time=details['closing']
            ))

# Bulk create to insert all vehicles in a single operation
Vehicle.objects.bulk_create(vehicles)
print("Vehicle table populated successfully with unique entries for each vehicle.")'''