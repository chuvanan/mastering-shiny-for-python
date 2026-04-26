from shiny import App, render, ui


app_ui = ui.page_fluid(
    ui.input_slider(id="x", label="If x is", min=1, max=50, value=30),
    ui.input_slider(id="y", label="and y is", min=1, max=50, value=20),
    "then, x times y is",
    ui.output_text(id="product"),
)


def server(input, output, session):
    @render.text
    def product():
        return input.x() * input.y()


app = App(app_ui, server)
