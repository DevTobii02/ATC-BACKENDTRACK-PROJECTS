#Gives Suggestion based on weather data provided
print("What's  The Weather Today Like ")
ask_weather_condition = input("What's The Weather Condition Like : ").lower() .capitalize()
if ask_weather_condition == "Sunny".capitalize().lower():
    print("Take Along Your Sunshades")
elif ask_weather_condition == "Raining".capitalize().lower():
    print("Stay Indoors")
elif ask_weather_condition == "Cloudy".capitalize().lower():
    print("Prepare For Rain Take Along Your Umbrella and RainCoats")