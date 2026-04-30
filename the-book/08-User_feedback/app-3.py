from shiny import App, render, ui, reactive
import time

app_ui = ui.page_fluid(
    ui.input_action_button("goodnight", label="Goodnight"),
)


def server(input, output, session):

    @reactive.effect
    @reactive.event(input.goodnight)
    def _():
        ui.notification_show("So long")
        time.sleep(2)
        ui.notification_show("Farewell", type="message")
        time.sleep(2)
        ui.notification_show("Auf Wiedersehen", type="warning")
        time.sleep(2)
        ui.notification_show("Adieu", type="error")


app = App(app_ui, server)
