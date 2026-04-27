import polars as pl
from dotenv import load_dotenv

load_dotenv()

from querychat import QueryChat

flights = pl.scan_parquet("flights-1m.parquet")

qc = QueryChat(flights, "flights", client="anthropic/claude-sonnet-4-5")
app = qc.app()
