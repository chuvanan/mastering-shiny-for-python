from shiny import App, render, ui
from faicons import icon_svg


# limited choices input
app_ui = ui.page_fluid(
    ui.input_radio_buttons(
        "rb",
        "Choose one:",
        choices={
            "angry": icon_svg("face-angry"),
            "happy": icon_svg("face-grin-beam"),
            "sad": icon_svg("face-sad-cry"),
        },
    )
)


def server(input, output, session):
    return True


app = App(app_ui, server)
