import pandas as pd
from etl.DB import Conn
from logs.log import load_log

def jsonload_to_sql(data):
    load_log.info("flatten the json format before Loading to DB!")

    df = pd.json_normalize(data)  
    
    load_log.info("Successfully loads the data into MYSQL DATABASE!") 
    return df.to_sql(name="weather_api",
                     con=Conn(),
                     if_exists="replace",
                     index=False)