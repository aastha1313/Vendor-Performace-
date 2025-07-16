import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s -%(message)s",
    filemode= "a"
)

engine = create_engine('sqlite:///inventory.db')


def ingest_db_chunked(file_path, table_name, engine, chunksize=100000):
    print(f"Processing {table_name}...")
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"✓ Inserted {table_name} into database.")


'''this load CSVs as DF and ingest into db'''
def load_raw_data():
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data/', file)
            table_name = file.replace('.csv', '')  # Remove extension
            logging.info(f'ingesting {file} in db')
            ingest_db_chunked(file_path, table_name, engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info('------------injestion complete------------')

    logging.info(f'total time taken :{total_time} minutes')


if __name__ == '__main__':
    load_raw_data
