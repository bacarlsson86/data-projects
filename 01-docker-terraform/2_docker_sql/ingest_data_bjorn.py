#!/usr/bin/env python
# coding: utf-8

import argparse
import os
import pandas as pd
import pyarrow.parquet as pq
from time import time
from sqlalchemy import create_engine

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'output.parquet'

    os.system(f"wget {url} -O {parquet_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    # Read file, read table from file and check schema
    file = pq.ParquetFile(parquet_name)
    table = file.read()

    # convert to pandas and check data 
    df = table.to_pandas() 
    df.info()

    # We will create the connection to our postgres database. then we feed cnction info
    # generate the SQL query for the specific server. SQLalchemy suports a variety of
    # servers. So we create an open SQL database connection object OR SQLAlchemy connectable 

    # Create 100k row batch
    batches_iter = file.iter_batches(batch_size=100000)
    batches_iter

    # take first batch from our iterator
    df = next(batches_iter).to_pandas()

    # insert values into the table 
    t_start = time()
    count = 0
    for batch in file.iter_batches(batch_size=100000):
        count += 1
        batch_df = batch.to_pandas()
        print(f'inserting batch {count}...')
        b_start = time()

        batch_df.to_sql(name=table_name, con=engine, if_exists='append')
        b_end = time()
        print(f'inserted! time taken {b_end-b_start:10.3f} seconds.\n')

    t_end = time()
    print(f'Completed! Total time taken was {t_end - t_start:10.3f} seconds for {count} batches.')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest parquet data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the parquet file')

    args = parser.parse_args()

    main(args)





