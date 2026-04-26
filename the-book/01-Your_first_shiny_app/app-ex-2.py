

from shiny import App, render, ui


app_ui = ui.page_fluid(
    ui.input_slider(
        id="x", label="If x is", min=1, max=50, value=30
    ),
    "then x times 5 is",
    ui.output_text(
        id="product"
    )
)


def server(input, output, session):

    @render.text
    def product():
        res = input.x() * 5
        return res


app = App(app_ui, server)