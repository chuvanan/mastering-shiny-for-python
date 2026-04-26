from shiny import App, render, ui
from polars import Series

# text output
app_ui = ui.page_fluid(ui.output_text("text"), ui.output_text_verbatim("code"))


def server(input, output, session):
    @render.text
    def text():
        return "Hello friend!"

    @render.text
    def code():
        num_seq = Series(name="x", values=range(1, 11))
        return num_seq.describe()


app = App(app_ui, server)
