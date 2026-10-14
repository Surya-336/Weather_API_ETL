from logs.log import transform_log

def transform_Data(data, city):

    transform_log.info("Transforming the Extracted data Started!")
    transformed = {
        "City" : city,
        "Longitude" : data["coord"]["lon"],
        "Latitude" : data["coord"]["lat"],
        "Description" : data["weather"][0]["description"],
        "Temperature": data["main"]["temp"],
        "Min_Temp" : data["main"]["temp_min"],
        "Max_Temp" : data["main"]["temp_max"],
        "Feels_Like" : data["main"]["feels_like"],
        "Humidity" : data["main"]["humidity"],
        "Wind_Speed" : data["wind"]["speed"]
    }

    transform_log.info("transforming the data Successfully completed")
    return transformed
    

