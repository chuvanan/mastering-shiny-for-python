from shiny import App, render, ui

animals = ["dog", "cat", "mouse", "bird", "other", "I hate animals"]


# limited choices input
app_ui = ui.page_fluid(
    ui.input_select("animal1", "What's your favourite animal?", animals),
    ui.input_select(
        "animal3",
        "What's your favourite animal? (multiple selection)",
        animals,
        multiple=True,
    ),
    ui.input_radio_buttons("animal2", "What's your favourite animal?", animals),
    ui.input_checkbox_group("animal4", "What's your favourite animal?", animals),
)


def server(input, output, session):
    return True


app = App(app_ui, server)
