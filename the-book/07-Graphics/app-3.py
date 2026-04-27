import rdatasets
from shiny import App, ui, render, req
import rdatasets
from plotnine import *
import numpy as np


app_ui = ui.page_fluid(
    ui.output_plot("plot", click=True, width="600px", brush=True),
    "Point coordinate is:",
    ui.output_text_verbatim("info"),
    "Brush area is:",
    ui.output_text_verbatim("area"),
    "Data is",
    ui.output_data_frame("brushed_data"),
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

    @render.text
    def area():
        req(input.plot_brush())
        xmin = np.round(input.plot_brush()["xmin"], 2)
        xmax = np.round(input.plot_brush()["xmax"], 2)
        ymin = np.round(input.plot_brush()["ymin"], 2)
        ymax = np.round(input.plot_brush()["ymax"], 2)
        return f"[{xmin}, {ymin},\n{xmax}, {ymax}]"

    @render.data_frame
    def brushed_data():
        req(input.plot_brush())
        xmin = np.round(input.plot_brush()["xmin"], 2)
        xmax = np.round(input.plot_brush()["xmax"], 2)
        ymin = np.round(input.plot_brush()["ymin"], 2)
        ymax = np.round(input.plot_brush()["ymax"], 2)
        res = mtcars[
            (mtcars["wt"].between(xmin, xmax)) & (mtcars["mpg"].between(ymin, ymax))
        ]
        return res


app = App(app_ui, server)
