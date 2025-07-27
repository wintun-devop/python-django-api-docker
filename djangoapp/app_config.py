import os
from dotenv import load_dotenv

#to get to ensure from .env
load_dotenv(override=True)



# getting data from env
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host_write=os.getenv("DB_HOST_WRITE")
db_host_read=os.getenv("DB_HOST_READ")


APP_SECRET_KEY=os.getenv("APP_SECRET_KEY")