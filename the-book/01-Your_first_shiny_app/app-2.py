

from shiny import App, ui, render, reactive
import rdatasets


dataset_lst = [i.removesuffix(".pkl") for i in rdatasets.items()]



app_ui = ui.page_fluid(
    ui.input_select(
        id="dataset",
        label="Dataset",
        choices=dataset_lst
    ),
    ui.output_text_verbatim(
        id="summary"
    ),
    ui.output_table(
        id="table"
    )
)

def server(input, output, session):

    @reactive.calc
    def dataset():
        return rdatasets.data(input.dataset())

    @render.text
    def summary():
        dta = dataset()
        return dta.describe()

    @render.table
    def table():
        return dataset()



app = App(app_ui, server)