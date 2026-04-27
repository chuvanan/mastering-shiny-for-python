import duckdb

con = duckdb.connect("app03/flights.duckdb")
con.execute("""
    CREATE TABLE flights AS
    SELECT * FROM read_parquet('app03/flights-1m.parquet')
""")
con.execute("SELECT COUNT(*) FROM flights").fetchone()
con.close()
