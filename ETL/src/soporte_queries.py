create_schema = '''CREATE SCHEMA IF NOT EXISTS bollos;'''
create_table = '''CREATE TABLE IF NOT EXISTS users (
    id_client INT PRIMARY KEY,
    id_product VARCHAR(4),
    amount INT,
    email VARCHAR(100),
    product_name VARCHAR(100),
    total FLOAT
);
'''
insert_users = '''INSERT INTO users (id_client, id_product, amount, email, product_name, total)
VALUES (%s, %s, %s, %s, %s, %s);'''