# Hierarchical select boxes
# Territory -> Customer -> Order -> Rows

import polars as pl
from shiny import App, render, ui, reactive
from pathlib import Path

sales = pl.read_csv(
    Path(__file__).parent / "sales_data_sample.csv",
    encoding="latin1",
)

territories = sorted(sales["TERRITORY"].unique().to_list())

app_ui = ui.page_fluid(
    ui.h3("Sales Drill-Down"),
    ui.layout_columns(
        ui.input_select("territory", "Territory", choices=territories),
        ui.input_select("customer", "Customer", choices=[]),
        ui.input_select("order", "Order", choices=[]),
        col_widths=4,
    ),
    ui.hr(),
    ui.output_data_frame("order_rows"),
)


def server(input, output, session):

    @reactive.calc
    def territory_data():
        return sales.filter(pl.col("TERRITORY") == input.territory())

    @reactive.calc
    def customer_data():
        return territory_data().filter(pl.col("CUSTOMERNAME") == input.customer())

    @reactive.effect
    def _():
        customers = sorted(territory_data()["CUSTOMERNAME"].unique().to_list())
        ui.update_select("customer", choices=customers)

    @reactive.effect
    def _():
        orders = sorted(customer_data()["ORDERNUMBER"].unique().cast(pl.Utf8).to_list())
        ui.update_select("order", choices=orders)

    @render.data_frame
    def order_rows():
        cols = [
            "ORDERLINENUMBER",
            "PRODUCTCODE",
            "PRODUCTLINE",
            "QUANTITYORDERED",
            "PRICEEACH",
            "SALES",
            "STATUS",
        ]
        if not input.order():
            return pl.DataFrame()
        else:
            return (
                customer_data()
                .filter(pl.col("ORDERNUMBER").cast(pl.Utf8) == input.order())
                .select(cols)
                .sort("ORDERLINENUMBER")
            )


app = App(app_ui, server)
