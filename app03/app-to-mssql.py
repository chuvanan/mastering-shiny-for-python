from querychat import QueryChat
from sqlalchemy import create_engine

# import pyodbc

server = "localhost"
database = "tempdb"
username = "SA"
password = "1q2w3e&R"
driver = "ODBC Driver 18 for SQL Server"

# sample pyodbc connect
# conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes')

engine = create_engine(
    url=f"mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver={driver}",
    connect_args={"TrustServerCertificate": "yes"},
)


qc = QueryChat(engine, "mssql", client="anthropic/claude-sonnet-4-5")
app = qc.app()
