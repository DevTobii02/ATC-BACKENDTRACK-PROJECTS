#This Program Converts Varius Units to Another
print("Below Are Available Units Of Conversion Available")
AvailableUnitConversion = ("1. Temperature", "2. Distance", "3. Weight")
for a in AvailableUnitConversion:
    print(a) 
ChooseConversion = input("Choose From The Above Listed Conversion Options : ").lower().strip()    
if ChooseConversion == "Temperature".strip().lower():
    print("Below Are Available Temperature Conversion") 
    TemperatureConversion = ("1. Degree Celcius To Degree Farenheit", "2. Degree Farenheit To Degree Celcius")
    for a in TemperatureConversion:
        print(a) 
    PickOption = input("Choose From The Above Provided Conversions : ")   
    if PickOption == "1":
        temp_celsius = float(input("Enter temperature in Celsius: "))
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")
    elif PickOption == "2":
        temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        temp_celsius = (temp_fahrenheit - 32) * 5/9
        print(f"{temp_fahrenheit}°F is equal to {temp_celsius}°C")
    else:
        print("Invalid option selected.")
    if PickOption == "A".lower().strip():
        print(PickOption)     
elif ChooseConversion == "Distance".strip().lower():
    print("Below Are Conversion Available In  Distance") 
    DistanceConversion = ("1. Meters To Kilometers", "2. Centimetre To Metre")
    for a in DistanceConversion:
        print(a)
    PickOption = input("Choose From The Provided Options Above : ") 
elif ChooseConversion == "Weight".lower().strip():
    print("Below Are Conversion Available In Weight")
    WeightConversion = ("1. Gram To Kilogram", "2. Kilogram To Gram", "3. Kilogram To Pounds") 
    for a in WeightConversion:
        print(a)
    PickOption = input("Choose From The Above Listed Conversion : ")    