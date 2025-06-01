from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
PORT = os.getenv('DB_PORT')
HOST = os.getenv('DB_HOST')
CATEGORY_WEB = 1
DB_URI = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/blog'
CATEGORY_SCHOOL = 2
SECRET_KEY = os.getenv('SECRET_KEY')
