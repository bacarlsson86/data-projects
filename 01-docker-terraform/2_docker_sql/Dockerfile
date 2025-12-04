FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY ingest_data_bjorn.py ingest_data_bjorn.py 

ENTRYPOINT [ "python", "ingest_data_bjorn.py" ]