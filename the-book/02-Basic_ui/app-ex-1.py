from shiny import App, render, ui

# text input
app_ui = ui.page_fluid(
    ui.input_text(id="name", label="What's your name?", placeholder="Nguyen Van A")
)


def server(input, output, session):
    return True


app = App(app_ui, server)
