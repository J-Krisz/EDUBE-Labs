mile = 1609.344 # meters
gallon = 3.785411784 # liters

def liters_100km_to_miles_gallon(liters):
    consumption = liters / gallon
    distance = 1000 * 100 / mile
    return distance/consumption

def miles_gallon_to_liters_100km(miles):
    km = miles * 1609.344 / 1000 / 100
    return gallon / km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
