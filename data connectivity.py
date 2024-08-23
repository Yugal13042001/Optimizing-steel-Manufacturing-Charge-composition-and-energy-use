
import pandas as pd
mba = pd.read_csv(r"C:\Users\shrad\Desktop\steel1.csv")
mba.info()
from sqlalchemy import create_engine, text


# Creating engine which connect to MySQL
user = 'root' # user name
pw = 'root28' # password
db = 'project' # database

# creating engine to connect database
# If any special characters are there in sql username and password
#engine = create_engine(f"mysql+pymysql://{user}:%s@localhost/{db}" % quote(f'{pw}'))
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")
mba.to_sql('steel', con = engine, if_exists = 'replace', chunksize = None, index= False)

sql = "SELECT * FROM steel";

df1 = pd.read_sql_query(sql, engine) 

df1 = pd.read_sql_query(text(sql), engine.connect()) 
