# Update functions — pattern 2: cascading selects
# Selecting a continent filters the country choices.

from shiny import App, reactive, render, ui

COUNTRIES = {
    "Asia": ["Japan", "Vietnam", "India", "Thailand"],
    "Europe": ["France", "Germany", "Italy", "Spain"],
    "Americas": ["Brazil", "Canada", "Mexico", "USA"],
}

app_ui = ui.page_fluid(
    ui.input_select("continent", "Continent", choices=list(COUNTRIES.keys())),
    ui.input_select("country", "Country", choices=COUNTRIES["Asia"]),
    ui.output_text("result"),
)


def server(input, output, session):

    @reactive.effect
    def _():
        choices = COUNTRIES[input.continent()]
        ui.update_select("country", choices=choices)

    @render.text
    def result():
        return f"You selected: {input.country()} ({input.continent()})"


app = App(app_ui, server)
