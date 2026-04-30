from shiny import App, render, ui, reactive, req

app_ui = ui.page_fluid(
    ui.input_numeric(id="n", label="n", min=1, max=100, value=10),
    ui.input_select("type", "type", choices=["default", "message", "warning", "error"]),
    ui.output_text(id="half"),
)


def server(input, output, session):

    @reactive.calc
    def res():
        req(input.n())
        return input.n() / 2

    @reactive.effect
    def _():
        req(input.n())
        ui.notification_show(
            "This notification will disappear after 2 seconds.",
            type=input.type(),
            duration=2,
        )

    @render.text
    def half():
        return res()


app = App(app_ui, server)
