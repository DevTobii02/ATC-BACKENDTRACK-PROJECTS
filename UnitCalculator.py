#This Program Converts Varius Units to Another
print("Below Are Available Units Of Conversion Available")
AvailableUnitConversion = ("1. Temperature", "2. Distance", "3. Weight")
for a in AvailableUnitConversion:
    print(a) 
ChooseConversion = input("Choose From The Above Listed Conversion Options : ").lower().strip()    
if ChooseConversion == "Temperature".strip().lower():
    print("Below Are Available Temperature Conversion") 
    TemperatureConversion = ("1. Degree Celcius To Degree Farenheit", "2. Degree Farenheit To Degree Celcius", "3. Kelvin To Celcius", "4. Celcius To Kelvin", "5. Farenheit To Kelvin", "6. Kelvin To Farenheit")
    for a in TemperatureConversion:
        print(a) 
    PickOption = input("Choose From The Above Provided Conversions : ")   
    if PickOption == "1":
        print("Converts From Degree Celcius To Degree Farenheit")
        temp_celsius = float(input("Enter temperature in Celsius: "))
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")
    elif PickOption == "2":
        print("Converts From Degree Farenheit To Degree Celcius")
        temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        temp_celsius = (temp_fahrenheit - 32) * 5/9
        print(f"{temp_fahrenheit}°F is equal to {temp_celsius}°C")
    elif PickOption == "3":
        print("Converts From Degree Celcius To Degree Kelvin")
        temp_celsius = float(input("Enter temperature in celcius"))
        temp_kelvin = ({temp_celsius} + 273.15)
        print(f"{temp_celsius}C  is equal to {temp_kelvin}K")
    elif PickOption == "4":
        print("Converts From Degree Kelvin To Degree Celcius")
        temp_kelvin = float(input("Enter temperature in kelvin : "))
        temp_celsius = ({temp_kelvin} - 273.15)
        print(f"your {temp_kelvin}K is equal to {temp_celsius}C")
    # Temperature Conversion Options

    elif PickOption == "5":
        print("Converts From Degree Farenheit To Degree Kelvin")
        # Convert Fahrenheit to Kelvin
        temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        temp_kelvin = (temp_fahrenheit - 32) * 5/9 + 273.15
        print(f"{temp_fahrenheit}°F is equal to {temp_kelvin} K")

    elif PickOption == "6":
        print("Converts From Degree Kelvin To Degree Fahrenheit")
        # Convert Kelvin to Fahrenheit
        temp_kelvin = float(input("Enter temperature in Kelvin: "))
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        print(f"{temp_kelvin} K is equal to {temp_fahrenheit}°F")
    else:
        print("Invalid option selected.")
elif ChooseConversion == "Distance".strip().lower():
    print("Below Are Conversion Available In  Distance") 
    DistanceConversion = ("1. Metres To Kilometres", "2. Kilmeters To Meters", "3. Centimetres To Meters", "4. Meters To Centiemeters")
    for a in DistanceConversion:
        print(a)
    PickOption = input("Choose From The Provided Options Above : ") 
    if PickOption == "1":
        print("Converts Metres To Kilometres")
        distance_in_metres = float(input("Enter Your Distance In Metres : "))
        distance_in_Kilometres = distance_in_metres / 1000
        print(f"{distance_in_metres}m is equal to {distance_in_Kilometres} km")
    elif PickOption == "2":
        print("Converts Kilometres To Metres")
        distance_in_Kilometres = float(input("Enter Distance In Kilometers : "))
        distance_in_metres  = distance_in_Kilometres * 1000
        print(f"{distance_in_Kilometres}km is equivalent to {distance_in_metres}m")
    elif PickOption == "3":
        print("Converts Centimetres To Metres")
        distance_in_Centimetres = float(input("Enter Distance In Centimetres"))
        distance_in_metres = distance_in_Centimetres / 100 
        print(f"{distance_in_Centimetres}cm Is Equal To {distance_in_metres}m")
    elif PickOption == "4" :
        distance_in_metres = float(input("Enter Distance In Meters : "))
        distance_in_Centimetres = distance_in_metres * 100
        print(f"{distance_in_metres}m Is equivalent To {distance_in_Centimetres}cm")
    else:
        print("Invalid Option")
elif ChooseConversion == "Weight".lower().strip():
    print("Below Are Conversion Available In Weight")
    WeightConversion = ("1. Gram To Kilogram", "2. Kilogram To Gram", "3. Kilogram To Pounds", "4. Pounds To Kilogram") 
    for a in WeightConversion:
        print(a)
    PickOption = input("Choose From The Above Listed Conversion : ")
    if PickOption == "1":
        print("Converts Weight In Gram To KiloGram")
        weight_in_gram = float(input("Enter Weight In Gram"))
        weight_in_kilogram = weight_in_gram / 1000 
        print(f"{weight_in_gram}g is equivalent to {weight_in_kilogram}kg")
    elif PickOption == "2":
        weight_in_kilogram = float(input("Enter Weight In Kilogram : "))
        weight_in_gram = weight_in_kilogram * 1000
        print(f"{weight_in_kilogram}kg Is equal to {weight_in_gram}g")
    else:
        print("Invalid Option") 