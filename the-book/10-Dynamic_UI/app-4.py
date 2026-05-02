# Update functions — pattern 4: update label and disabled state
# Disable/enable a button based on form validity; update its label too.

from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_text("username", "Username (min 3 chars)", value=""),
    ui.input_password("password", "Password (min 6 chars)", value=""),
    ui.input_action_button("login", "Log in", disabled=True),
    ui.output_text("status"),
)


def server(input, output, session):

    @reactive.calc
    def valid():
        return len(input.username()) >= 3 and len(input.password()) >= 6

    @reactive.effect
    def _():
        if valid():
            ui.update_action_button("login", label="Log in", disabled=False)
        else:
            ui.update_action_button("login", label="Fill in the form", disabled=True)

    @render.text
    @reactive.event(input.login)
    def status():
        return f"Logged in as '{input.username()}'"


app = App(app_ui, server)
