from src import soporte_sql as sql
from src import soporte_queries as queries
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

df = pd.read_csv('files/df_final.csv')

lista_datos = df[['ID_Cliente','id_product', 'amount', 'email', 'product_name', 'total']].to_records(index=False).tolist()

sql.creacion_bbdd_tablas(queries.create_schema, )