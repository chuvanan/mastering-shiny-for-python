from dotenv import load_dotenv

load_dotenv()

from querychat import QueryChat
from sqlalchemy import create_engine

# Use query chat with local database file

engine = create_engine("duckdb:///flights.duckdb")

qc = QueryChat(engine, "flights", client="anthropic/claude-sonnet-4-5")
app = qc.app()
