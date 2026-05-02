# Update functions — pattern 3: button resets a form
# A Reset button restores all inputs to their defaults.

from shiny import App, reactive, render, ui

DEFAULTS = {"name": "", "age": 25, "agree": False}

app_ui = ui.page_fluid(
    ui.input_text("name", "Name", value=DEFAULTS["name"]),
    ui.input_numeric("age", "Age", value=DEFAULTS["age"], min=0, max=120),
    ui.input_checkbox("agree", "I agree to the terms", value=DEFAULTS["agree"]),
    ui.input_action_button("reset", "Reset"),
    ui.input_action_button("submit", "Submit"),
    ui.output_text("summary"),
)


def server(input, output, session):

    @reactive.effect
    @reactive.event(input.reset)  # only fires when Reset is clicked
    def _():
        ui.update_text("name", value=DEFAULTS["name"])
        ui.update_numeric("age", value=DEFAULTS["age"])
        ui.update_checkbox("agree", value=DEFAULTS["agree"])

    @render.text
    @reactive.event(input.submit)
    def summary():
        return f"{input.name()}, age {input.age()}, agreed={input.agree()}"


app = App(app_ui, server)
