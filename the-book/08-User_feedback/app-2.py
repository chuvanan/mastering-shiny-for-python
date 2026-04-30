from shiny import App, Inputs, Outputs, Session, render, ui, req


app_ui = ui.page_fluid(
    ui.input_select("language", "Language", choices=["", "English", "Maori"]),
    ui.input_text("name", "Name"),
    ui.output_text("greeting"),
    ui.help_text(
        "Note: while the data view will show only the specified number of observations, the summary will be based on the full dataset."
    ),
)


def server(input=Inputs, output=Outputs, session=Session):

    greetings = {"English": "Hello", "Maori": "Kia ora"}

    @render.text
    def greeting():
        req(input.language(), input.name())
        return f"{greetings[input.language()]} {input.name()} !"


app = App(app_ui, server)
