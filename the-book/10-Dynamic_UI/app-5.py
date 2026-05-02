from shiny import App, render, ui, reactive


app_ui = ui.page_fluid(
    ui.input_numeric("n", "Simulations", 10),
    ui.input_action_button("simulate", "Simulate"),
)


def server(input, output, session):

    @reactive.effect
    @reactive.event(input.n)
    def _():
        ui.update_action_button(id="simulate", label=f"Simulate {input.n()} times")


app = App(app_ui, server)
