mile_in_kms = 1.60934
km_in_miles = 0.621371

print("How many kilometers did you run today?")
kms = input()
miles = float(kms) / mile_in_kms
rounded_miles = round(miles, 2)
print(f"Your {kms} kilometres run is equal to {rounded_miles} miles.")
