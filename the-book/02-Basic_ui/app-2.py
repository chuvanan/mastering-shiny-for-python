


from shiny import App, render, ui

# numeric input
app_ui = ui.page_fluid(
    ui.input_numeric("num", "Number one", value = 0, min = 0, max = 100),
    ui.input_slider("num2", "Number two", value = 50, min = 0, max = 100),
    ui.input_slider("rng", "Range", value = [10, 20], min = 0, max = 100)
)


def server(input, output, session):
    return True


app = App(app_ui, server)
