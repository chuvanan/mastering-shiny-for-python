from shiny import App, render, ui
import rdatasets

# data table output
app_ui = ui.page_fluid(ui.output_table("static"), ui.output_data_frame("dynamic"))


def server(input, output, session):
    @render.table
    def static():
        mtcars = rdatasets.data("mtcars")
        return mtcars.head(6)

    @render.data_frame
    def dynamic():
        mtcars = rdatasets.data("mtcars")
        return render.DataTable(mtcars.head(6))


app = App(app_ui, server)
