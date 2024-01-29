from testcontainers.postgres import PostgresContainer
import psycopg


# pytest for testcontainers connection
with PostgresContainer('postgres:11.1') as postgres:
    engine = psycopg.connect(
        database=postgres.database_name,
        user=postgres.username,
        password=postgres.password,
        host=postgres.host,
        port=postgres.port
    )
    cursor = engine.cursor()
    cursor.execute('SELECT version()')
    result = cursor.fetchone()
    print(result)