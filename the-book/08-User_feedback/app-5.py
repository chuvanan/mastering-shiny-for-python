from shiny import App, render, ui, reactive
import time
import rdatasets

app_ui = ui.page_fluid(ui.output_data_frame("data"))


def server(input, output, session):

    def notify(msg, id=None):
        return ui.notification_show(msg, id=id, duration=None, close_button=False)

    @reactive.calc
    def gen_data():
        try:
            id = notify("Reading data...")
            time.sleep(2)

            notify("Reticulating splines...", id=id)
            time.sleep(2)

            notify("Herding llamas...", id=id)
            time.sleep(2)

            notify("Orthogonalizing matrices...", id=id)
            time.sleep(2)

            mtcars = rdatasets.data("mtcars")
            return mtcars
        finally:
            ui.notification_remove(id)

    @render.data_frame
    def data():
        return gen_data().head()


app = App(app_ui, server, debug=True)
