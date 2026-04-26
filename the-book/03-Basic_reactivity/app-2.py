# example code for understanding reactive graph and reactive expression

from shiny import App, render, ui, reactive
from shared import freqpoly, t_test
import numpy as np

app_ui = ui.page_fluid(
    ui.row(
        ui.column(
            4,
            "Distribution 1",
            ui.input_numeric("n1", label="n", value=1000, min=1),
            ui.input_numeric("mean1", label="µ", value=0, step=0.1),
            ui.input_numeric("sd1", label="σ", value=0.5, min=0.1, step=0.1),
        ),
        ui.column(
            4,
            "Distribution 2",
            ui.input_numeric("n2", label="n", value=1000, min=1),
            ui.input_numeric("mean2", label="µ", value=0, step=0.1),
            ui.input_numeric("sd2", label="σ", value=0.5, min=0.1, step=0.1),
        ),
        ui.column(
            4,
            "Frequency polygon",
            ui.input_numeric("binwidth", label="Bin width", value=0.1, step=0.1),
            ui.input_slider("range", label="range", value=[-3, 3], min=-5, max=5),
        ),
    ),
    ui.row(
        ui.column(9, ui.output_plot("hist")),
        ui.column(3, ui.output_text_verbatim("ttest")),
    ),
)


def server(input, output, session):
    @reactive.calc
    def x1():
        return np.random.normal(loc=input.mean1(), scale=input.sd1(), size=input.n1())

    @reactive.calc
    def x2():
        return np.random.normal(loc=input.mean2(), scale=input.sd2(), size=input.n2())

    @render.plot
    def hist():
        return freqpoly(x1(), x2(), binwidth=input.binwidth(), xlim=input.range())

    @render.text
    def ttest():
        return t_test(x1(), x2())


app = App(app_ui, server)
