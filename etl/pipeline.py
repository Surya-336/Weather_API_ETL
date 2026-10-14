from etl.extract import get_request
from etl.transform import transform_Data
from etl.load import jsonload_to_sql
from logs.log import pipeline_log

cities = ["Chennai","Pune","Delhi","Mumbai","Bengaluru","Puducherry","Nashik","Amritsar","Varanasi",
          "Ludhiana","Madurai","Salem","Hyderabad","Kolkata","Visakhapatnam","Chandigarh",
          "Ahmedabad","Kochi","Guwahati","Nellore","Ranchi","Lucknow","Hosur",
          "Coimbatore","Mysuru","Indore","Surat","Bhopal","Warangal","Vijayawada","Agra"]

def run_pipeline():
    extracted = []

    for city in cities:
        try:
            raw = get_request(city)
            transform = transform_Data(raw,city)
            extracted.append(transform)


        except Exception as e:
            print(f"AN Error In {city}, {e}") 

    if extracted:
        jsonload_to_sql(extracted)
    else:
        print("No weather data collected; skipping SQL load.")

if __name__ == "__main__":

    pipeline_log.info("Pipeline Started Running")

    run_pipeline()
    pipeline_log.info("Pipleline Succesfully completed")