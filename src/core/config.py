import os

API_STR = "/api"

# Database config
# POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
# POSTGRES_USER = os.getenv("POSTGRES_USER")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
# POSTGRES_DB = os.getenv("POSTGRES_DB")
DATABASE_URL = os.environ.get('DATABASE_URL')
# DATABASE_URL = (
#     f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
# )
