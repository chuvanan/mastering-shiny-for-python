

# Shiny app is extremely lazy
# Read reactive graph to understand order of execution


from shiny import App, render, ui, reactive


app_ui = ui.page_fluid(
    ui.input_text("name", "What's your name?"),
    ui.output_text("greeting")
)


# example where order of execution is not linear
def server(input, output, session):

    @render.text
    def greeting():
        return your_name()

    @reactive.calc
    def your_name():
        return f"Hello {input.name()}!"


app = App(app_ui, server)