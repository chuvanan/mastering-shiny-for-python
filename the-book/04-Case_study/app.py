from shiny import App, render, ui, reactive
import polars as pl
from plotnine import *


injuries = pl.read_csv("the-book/04-Case_study/neiss/injuries.tsv.gz", separator="\t")
injuries = injuries.with_columns(prod_code=pl.col("prod_code").cast(pl.String))
products = pl.read_csv("the-book/04-Case_study/neiss/products.tsv", separator="\t")
population = pl.read_csv("the-book/04-Case_study/neiss/population.tsv", separator="\t")

product_codes = dict(zip(products["prod_code"], products["title"]))


app_ui = ui.page_fluid(
    ui.row(
        ui.column(
            8, ui.input_select("code", "Product", choices=product_codes, width="100%")
        ),
        ui.column(2, ui.input_select("y", "Y axis", ["rate", "count"], width="100%")),
    ),
    ui.row(
        ui.column(4, ui.output_data_frame("diag")),
        ui.column(4, ui.output_data_frame("body_part")),
        ui.column(4, ui.output_data_frame("location")),
    ),
    ui.row(ui.column(12, ui.output_plot("age_sex", width="600px"))),
    ui.row(
        ui.column(2, ui.input_action_button("story", "Tell me a story")),
        ui.column(10, ui.output_text("narrative")),
    ),
)


def server(input, output, session):
    @reactive.calc
    def selected():
        res = injuries.filter(pl.col("prod_code") == input.code())
        return res

    @reactive.calc
    def agg_():
        res = (
            selected()
            .group_by(["age", "sex"])
            .agg(n=pl.col("weight").sum())
            .join(population, how="left", on=["age", "sex"])
            .with_columns(rate=pl.col("n") / pl.col("population") * 1e4)
        )
        return res

    @render.data_frame
    def diag():
        res = (
            selected()
            .group_by("diag")
            .agg(n=pl.col("weight").sum().cast(pl.Int32))
            .sort(by="n", descending=True)
            .head(5)
        )
        return res

    @render.data_frame
    def body_part():
        res = (
            selected()
            .group_by("body_part")
            .agg(n=pl.col("weight").sum().cast(pl.Int32))
            .sort(by="n", descending=True)
            .head(5)
        )
        return res

    @render.data_frame
    def location():
        res = (
            selected()
            .group_by("location")
            .agg(n=pl.col("weight").sum().cast(pl.Int32))
            .sort(by="n", descending=True)
            .head(5)
        )
        return res

    @render.plot
    def age_sex():
        if input.y() == "rate":
            p = (
                ggplot(agg_().to_pandas(), aes("age", "rate", color="sex"))
                + geom_line()
                + labs(y="Injuries per 10,000 people")
            )
        else:
            p = (
                ggplot(agg_().to_pandas(), aes("age", "n", color="sex"))
                + geom_line()
                + labs(y="Estimated number of injuries")
            )
        return p

    @render.text
    @reactive.event(input.story)
    def narrative():
        sample_narr = selected()["narrative"].sample(1)[0]
        return sample_narr


app = App(app_ui, server)
