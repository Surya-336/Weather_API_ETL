import csv
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("Base_url")
api_key = os.getenv("API_KEY")

def get_request(city,country="IN"):
    
    if not api_key:
        raise RuntimeError("Set API_KEY in your environment or .env file")

    response = requests.get(
        url,
        params={
            "q": f"{city},{country}",
            "limit": 1,
            "appid": api_key,
            "units":"metric"
        },

        timeout=10
    )
    if not response.ok:
        raise RuntimeError(f"OpenWeatherMap request failed: HTTP {response.status_code}")
    forecast = response.json()

    with open("Data.json", "w", encoding="utf-8") as output:
        json.dump(forecast, output, indent=2, ensure_ascii=False)

    return forecast

def get_city_weather(city, Country="IN"):

    #api_key = os.getenv("API_KEY") 
    #_url = f"https://api.openweathermap.org/data/2.5/weather?q=Kerala##,IN&appid={api_key}&units=metric"
    get_data = requests.get(url,
                            params={"q":f"{city},{Country}","appid":api_key,
                            "units":"metric"},
                            timeout=10)
    
    if not api_key:
        raise RuntimeError("This is Runtime Error bcause of No API_KEY")

    get_data.raise_for_status()
    return get_data.json()


def load_to_Csv(city):

    with open("Weather_BY_City.csv", "w", newline="") as CsvFile:
        write = csv.writer(CsvFile)
        dictRead = csv.DictWriter(get_request(city))
        write.writerows(dictRead)

    

if __name__ == "__main__":
    #get_request("Chennai", "TN", "IN")
    #get_city_weather()
    
    cities1 = ["Chennai","Pune","Delhi","Mumbai","Bengaluru","Puducherry","Visakhapatnam","Madurai","Salem"]
    cities2 = ["Hyderabad","Kolkata","Ahmedabad","Kochi","Guwahati","Nellore","Ranchi","Lucknow","Hosur"]
    cities = cities1 + cities2
    extracted_Data = []
    
    for citys in cities:
          
        try:
            my_req = get_request(citys)
            extracted_Data.append({"City" : citys,
                    "Longitude" :my_req["coord"]["lon"],
                    "Latitude" : my_req["coord"]["lat"],
                    "Description" : my_req["weather"][0]["description"],
                    "Temperature": my_req["main"]["temp"],
                    "Min_Temp" : my_req["main"]["temp_min"],
                    "Max_Temp" : my_req["main"]["temp_max"],
                    "Feels_Like" : my_req["main"]["feels_like"],
                    "Humidity" : my_req["main"]["humidity"],
                    "Wind_Speed" : my_req["wind"]["speed"]
                }

            )
                   

        except requests.RequestException as e:
                print(F"AN Error {e}")

        with open("new_data.json", "w",newline="",encoding="utf-8") as JsonFile:        

            json.dump(extracted_Data, JsonFile, indent=2,ensure_ascii=False)

             


    
    

  


