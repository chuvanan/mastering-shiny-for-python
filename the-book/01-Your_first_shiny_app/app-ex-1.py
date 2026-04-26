

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_text(
        id="name", label="What's your name?"
    ),
    ui.output_text("greeting")
)


def server(input, output, session):

    @render.text
    def greeting():
        return f"Hello, {input.name()}"


app = App(app_ui, server)
