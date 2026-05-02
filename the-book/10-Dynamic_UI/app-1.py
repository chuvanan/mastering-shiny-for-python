# Dynamic UI
# updating inputs

from shiny import App, render, ui, reactive
import numpy as np

app_ui = ui.page_fluid(
    ui.input_numeric("min", "Minimum", 0),
    ui.input_numeric("max", "Maximum", 3),
    ui.input_slider("n", "n", min=0, max=3, value=1),
)


def server(input, output, session):

    @reactive.effect
    def _():
        ui.update_slider("n", min=input.min(), max=input.max(), value=input.n())


app = App(app_ui, server)
