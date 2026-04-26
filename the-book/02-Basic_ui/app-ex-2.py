from shiny import App, render, ui
import datetime

# date input
app_ui = ui.page_fluid(
    ui.input_slider(
        id="date",
        label="When should we deliver?",
        min=datetime.date(2020, 9, 1),
        max=datetime.date(2020, 9, 30),
        value=datetime.date(2020, 9, 3),
    )
)


def server(input, output, session):
    return True


app = App(app_ui, server)
