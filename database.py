import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
load_dotenv()

engine = create_engine(os.getenv('DB_URI'), echo=True, future=True)
