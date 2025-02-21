from dotenv import load_dotenv
load_dotenv()
import json
import os
#CAR_PREDICT_URL = "http://0.0.0.0:7860/predict"
CAR_PREDICT_URL = "https://wilmars-car-predict.hf.space/predict"
MOT_PREDICT_URL = "https://wilmars-mot-predict.hf.space/predict"


with open('src/data.json', 'r') as f:
    all_makes = json.load(f)

with open('src/data_motos.json', 'r') as f:
    all_makes_motos = json.load(f)

all_models = [1954, 1966, 1971, 1977, 1980, 1981, 1982, 1984, 1985, 1986, 1987,
       1988, 1989, 1990, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
       2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
       2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022,
       2023, 2024, 2025]

DATABASE_CONFIG = {
    "dbname": os.environ['DB_NAME'],
    "user":  os.environ['USER_NAME'],
    "password":  os.environ['PASSWORD'],
    "host":  os.environ['HOST']
}