import rdatasets
from shiny import App, ui, render, req
import rdatasets
from plotnine import *
import numpy as np

app_ui = ui.page_fluid(
    ui.output_plot("plot", click=True, width="600px"), ui.output_text_verbatim("info")
)


def server(input, output, session):
    mtcars = rdatasets.data("mtcars")

    @render.plot
    def plot():
        p = ggplot(mtcars, aes("wt", "mpg")) + geom_point()
        return p

    @render.text
    def info():
        req(input.plot_click())
        x = np.round(input.plot_click()["x"], 2)
        y = np.round(input.plot_click()["y"], 2)
        return f"[{x}, {y}]"


app = App(app_ui, server)
