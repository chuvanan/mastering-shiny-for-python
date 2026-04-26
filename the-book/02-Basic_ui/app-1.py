from shiny import App, render, ui

# text input
app_ui = ui.page_fluid(
    ui.input_text(id="name", label="What's your name?"),
    ui.input_password(id="password", label="What's your password?"),
    ui.input_text_area(id="story", label="Tell me about yourself", rows=3),
)


def server(input, output, session):
    return True


app = App(app_ui, server)
