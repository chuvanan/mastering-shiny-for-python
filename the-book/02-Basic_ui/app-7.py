





from shiny import App, render, ui
from faicons import icon_svg


# file upload and action button
app_ui = ui.page_fluid(
    ui.input_file("upload", None),
    ui.input_action_button("click", "Click me!", class_="btn-danger"),
    ui.input_action_button("drink", "Drink me!", class_="btn-success"),
)


def server(input, output, session):
    return True


app = App(app_ui, server)
