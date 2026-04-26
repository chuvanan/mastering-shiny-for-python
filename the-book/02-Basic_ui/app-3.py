from shiny import App, render, ui

# date input
app_ui = ui.page_fluid(
    ui.input_date("dob", "When were you born?"),
    ui.input_date_range("holiday", "When do you want to go on vacation next?"),
)


def server(input, output, session):
    return True


app = App(app_ui, server)
