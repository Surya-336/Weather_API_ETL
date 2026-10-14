from sqlalchemy import URL, create_engine
import os
from dotenv import load_dotenv


load_dotenv()

engine = None

def Conn():
    global engine

    if engine is None:
        print("Creating a New Db Engine")

        settings = {
            "DB_Host": os.getenv("DB_Host"),
            "DB_Pwd": os.getenv("DB_Pwd"),
            "DB_User": os.getenv("DB_User"),
            "DB": os.getenv("DB"),
        }
        missing = [key for key, value in settings.items() if not value]
        if missing:
            raise RuntimeError(f"Missing database settings: {', '.join(missing)}")

        engine = create_engine(
            URL.create(
                "mysql+pymysql",
                username=settings["DB_User"],
                password=settings["DB_Pwd"],
                host=settings["DB_Host"],
                database=settings["DB"],
            )
        )

    return engine