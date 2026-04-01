import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
import logging
from dotenv import load_dotenv
import urllib.parse


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_SERVER = os.getenv('DB_SERVER', 'DESKTOP-6RRSB8S\\SQLEXPRESS01')
DB_PORT = os.getenv('DB_PORT', '1433')
DB_NAME = os.getenv('DB_NAME', 'routine4life')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')
DB_DRIVER = os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server')



# Construir cadena de conexión
connection_string = (
    f"DRIVER={DB_DRIVER};"
    f"SERVER={DB_SERVER},{DB_PORT};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    #f"Trusted_Connection=yes;"  
    #f"TrustServerCertificate=yes;"
    
)

#connection_string = (
    #r'Driver={ODBC Driver 17 for SQL Server};'
    #r'Server=.\DESKTOP-6RRSB8S\SQLEXPRESS01;' # Replace with your server name
    #r'Database=routine4life;'
    #r'Trusted_Connection=yes;'
#)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
#DATABASE_URL = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

#odbc_connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server=tcp:{DB_SERVER},1433;Database={DB_NAME};Uid={DB_USER};Pwd={DB_PASSWORD};Encrypt=no;TrustServerCertificate=yes;Connection Timeout=30;"  

#DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(odbc_connection_string)}"

logger.info(f"Conectando a: {DB_SERVER}:{DB_PORT}/{DB_NAME} con usuario: {DB_USER} y password: {DB_PASSWORD} ")

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=3600
)

# Probar conexión
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        logger.info("Conexión a SQL Server exitosa")
except Exception as e:
    logger.error(f"Error de conexión: {e}")

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()