from plotnine import geom_point
from shiny import App, render, ui
import rdatasets
from plotnine import *

# plot output
app_ui = ui.page_fluid(ui.output_plot("plot", width="700px", height="300px"))


def server(input, output, session):
    cars = rdatasets.data("cars")

    @render.plot(alt="Scatter plot with width=700px and height=300px")
    def plot():
        p = ggplot(cars, aes("speed", "dist")) + geom_point()
        return p


app = App(app_ui, server)
