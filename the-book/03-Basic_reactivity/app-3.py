# control timing of evaluation


from shiny import App, render, ui, reactive
from shared import freqpoly, t_test
import numpy as np


app_ui = ui.page_fluid(
    ui.row(
        ui.column(
            3,
            ui.input_numeric("lambda1", label="lambda1", value=3),
            ui.input_numeric("lambda2", label="lambda2", value=5),
            ui.input_numeric("n", label="n", value=1e4, min=0),
        ),
        ui.column(9, ui.output_plot("hist")),
    )
)


def server(input, output, session):
    @reactive.calc
    def x1():
        reactive.invalidate_later(0.5)
        return np.random.poisson(lam=input.lambda1(), size=input.n())

    @reactive.calc
    def x2():
        reactive.invalidate_later(0.5)
        return np.random.poisson(lam=input.lambda2(), size=input.n())

    @render.plot
    def hist():
        return freqpoly(x1(), x2(), binwidth=1, xlim=(0, 40))


app = App(app_ui, server)
