mileInKms = 1.60934
kmInMiles = 0.621371

print("How many kilometers did you run today?")
kms = input()
miles = float(kms) / mileInKms
roundedMiles = round(miles, 2)
print(f"Your {kms} kilometres run is equal to {roundedMiles} miles.")
