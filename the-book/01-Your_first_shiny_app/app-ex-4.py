from shiny import App, render, ui, reactive


app_ui = ui.page_fluid(
    ui.input_slider(id="x", label="If x is", min=1, max=50, value=30),
    ui.input_slider(id="y", label="and y is", min=1, max=50, value=5),
    "then, (x * y) is",
    ui.output_text(id="product"),
    "and, (x * y) + 5 is",
    ui.output_text(id="product_plus5"),
    "and, (x * y) + 10 is",
    ui.output_text(id="product_plus10"),
)


def server(input, output, session):
    @reactive.calc
    def x_times_y():
        return input.x() * input.y()

    @render.text
    def product():
        return x_times_y()

    @render.text
    def product_plus5():
        return x_times_y() + 5

    @render.text
    def product_plus10():
        return x_times_y() + 10


app = App(app_ui, server)
