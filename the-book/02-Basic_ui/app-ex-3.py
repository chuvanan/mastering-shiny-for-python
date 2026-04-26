

from shiny import App, render, ui


# slider input with animation
app_ui = ui.page_fluid(
    ui.input_slider(
        id="num",
        label="What's your lucky number?",
        min=0,
        max=100,
        value=5,
        step=5,
        animate=True
    )
)


def server(input, output, session):
    return True


app = App(app_ui, server)
