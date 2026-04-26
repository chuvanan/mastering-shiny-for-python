

from shiny import App, Inputs, Outputs, Session, ui


app_ui = ui.page_fluid(
    "Hello world"
)

def server(input: Inputs, output: Outputs, session: Session):
    return True


app = App(app_ui, server)