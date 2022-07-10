import requests
import json
import datetime

api_key = input("Type your API key of Open Weather Map: ")

run_again = "Y"
while run_again == "Y":
    city = input("Forecast which city?: ")
    print("\nCharging...\n")

    call_link = f"https://api.openweathermap.org/data/2.5/forecast?q={city}\
&units=imperial&appid={api_key}"

    json_requisition = requests.get(call_link)
    forecast_info = json.loads(json_requisition.text)

    response_code = forecast_info['cod']

    if response_code == "200":
        pass

    else:
        print(f"""\nCode Error: {forecast_info['cod']} \nSee https://openweathermap.org/faq/#api-errors \
for more details""")

        run_again = input("\nTry Again? Y or N?: ").upper()

        if run_again == "Y":

            print("\n<><><><><><><><><><><><><><><><><><><><><>\n")

        else:
            run_again = "N"

    country = forecast_info['city']['country']

    city = forecast_info['city']['name']

    city_id = forecast_info['city']['id']

    latitude, longtude = forecast_info['city']['coord']['lat'], forecast_info['city']['coord']['lon']

    population = forecast_info['city']['population']

    timezone = forecast_info['city']['timezone'] / 3600


    def unix_timestamp_conversion(unix_time):
        unix = int(unix_time)

        date_time = datetime.datetime.fromtimestamp(unix)

        converted_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

        return converted_time


    sunrise = unix_timestamp_conversion(forecast_info['city']['sunrise'])

    sunset = unix_timestamp_conversion(forecast_info['city']['sunset'])


    #--------------------------------------------------------------------------------------------------


    def date_and_time(index):
        dt_txt_data = forecast_info['list'][index]['dt_txt']
        return dt_txt_data


    def weather(index):
        weather_data = forecast_info['list'][index]['weather'][0]['main']
        return weather_data


    def descripition(index):
        descripition_data = forecast_info['list'][index]['weather'][0]['description']
        return descripition_data


    def temperature(index):
        temperature_data = forecast_info['list'][index]['main']['temp']
        return temperature_data


    def minimal(index):
        temp_min_data = forecast_info['list'][index]['main']['temp_min']
        return temp_min_data


    def maximum(index):
        temp_max_data = forecast_info['list'][index]['main']['temp_max']
        return temp_max_data


    def feels_like(index):
        fells_like_data = forecast_info['list'][index]['main']['feels_like']
        return fells_like_data


    # --------------------------------------------------------------------------------------------------


    def clouds(index):
        cloads_data = forecast_info['list'][index]['wind']['speed']
        return cloads_data


    def humidity(index):
        humidity_data = forecast_info['list'][index]['main']['humidity']
        return humidity_data


    def visibility(index):
        visibility_data = forecast_info['list'][index]['visibility']
        return visibility_data


    def wind_spd(index):
        wind_speed_data = forecast_info['list'][index]['wind']['speed']
        return wind_speed_data


    def wind_deg(index):
        wind_degrees_data = forecast_info['list'][index]['wind']['deg']
        return wind_degrees_data


    def wind_gust(index):
        wind_gusts_data = forecast_info['list'][index]['wind']['gust']
        return wind_gusts_data


    # --------------------------------------------------------------------------------------------------


    def pressure(index):
        pressure_data = forecast_info['list'][index]['main']['pressure']
        return pressure_data


    def sea_level(index):
        sea_level_data = forecast_info['list'][index]['main']['sea_level']
        return sea_level_data


    def ground_level(index):
        ground_level_data = forecast_info['list'][index]['main']['grnd_level']
        return ground_level_data


    print(f"""
Lat, Lon:     {latitude}, {longtude}
          
Country:      {country}
City:         {city}
City ID:      {city_id}

Timezone:     {timezone:.0f} hours
Population:   {population:,}

Sunrise:      {sunrise}
Sunset:       {sunset}

    """)

    max_index = len(forecast_info['list'])

    for recorded_hours in range(1, max_index):
        print(f"""
-----------------------------------------
-----------{date_and_time(recorded_hours)}-----------
-----------------------------------------
Weather:            {weather(recorded_hours)}
Descripition:       {descripition(recorded_hours)}
Temperature:        {temperature(recorded_hours)} F°
Min and Max Temp:   {minimal(recorded_hours)} F° - {maximum(recorded_hours)} F°
Feels Like:         {feels_like(recorded_hours)} F°

Clouds:             {clouds(recorded_hours)}%
Humidity:           {humidity(recorded_hours)}%
Visibility:         {visibility(recorded_hours)} mi                                          
Wind Speed:         {wind_spd(recorded_hours)} mph
Wind Direction:     {wind_deg(recorded_hours)}°
Wind Gust:          {wind_gust(recorded_hours)} mph
                                        
Pressure:           {pressure(recorded_hours)} hPa
Sea Level:          {sea_level(recorded_hours)} hPa
Ground Level:       {ground_level(recorded_hours)} hPa
-----------------------------------------
    """)

    txt_confirmation = input("Want to save the forecast in a text file? Y or N?: ").upper()

    if txt_confirmation == "Y":
        time_now = datetime.datetime.now()
        time_now = time_now.strftime("%Y-%m-%d - %H.%M.%S")
        file = open(f"Forecast for {city} ({time_now}).txt", "a", encoding="utf-8")
        file.write(f"""Lat, Lon:     {latitude}, {longtude}
              
Country:      {country}
City:         {city}
City ID:      {city_id}

Timezone:     {timezone:.0f} hours
Population:   {population:,}

Sunrise:      {sunrise}
Sunset:       {sunset}
    """)
        for recorded_hours in range(1, max_index):
            file.write(f"""
-----------------------------------------
-----------{date_and_time(recorded_hours)}-----------
-----------------------------------------
Weather:            {weather(recorded_hours)}
Descripition:       {descripition(recorded_hours)}
Temperature:        {temperature(recorded_hours)} F°
Min and Max Temp:   {minimal(recorded_hours)} F° - {maximum(recorded_hours)} F°
Feels Like:         {feels_like(recorded_hours)} F°

Clouds:             {clouds(recorded_hours)}%
Humidity:           {humidity(recorded_hours)}%
Visibility:         {visibility(recorded_hours)} mi                                          
Wind Speed:         {wind_spd(recorded_hours)} mph
Wind Direction:     {wind_deg(recorded_hours)}°
Wind Gust:          {wind_gust(recorded_hours)} mph
                                        
Pressure:           {pressure(recorded_hours)} hPa
Sea Level:          {sea_level(recorded_hours)} hPa
Ground Level:       {ground_level(recorded_hours)} hPa
-----------------------------------------

    """)

    else:
        pass

    run_again = input("\nSee forecast for another city? Y or N?: ").upper()

    if run_again == "Y":

        print("\n<><><><><><><><><><><><><><><><><><><><><>\n")

    else:
        run_again = "N"
