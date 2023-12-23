import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
	
    DB_USERNAME : str = os.getenv("USERNAME")
    DB_PASSWORD = os.getenv("PASSWORD")
    DB_HOST : str = os.getenv("HOST","localhost")
    DB_PORT : str = os.getenv("PORT",3306)
    DB_DATABASE : str = os.getenv("DATABASE")
	
    DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

settings = Settings()