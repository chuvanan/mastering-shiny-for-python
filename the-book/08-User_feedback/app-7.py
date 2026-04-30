from shiny import App, ui, reactive, render
import asyncio

app_ui = ui.page_fluid(
    ui.input_text_area("message", "Enter Tweet", value=""),
    ui.input_action_button("tweet", "Tweet"),
)

def server(input, output, session):
    # Reactive values to track the state of the "pending" tweet
    last_message = reactive.Value("")
    waiting_task = reactive.Value(None)

    @reactive.Effect
    @reactive.event(input.tweet)
    def handle_tweet():
        msg = input.message()
        if not msg:
            return

        last_message.set(msg)
        ui.update_text_area("message", value="")

        # Show the notification with an Undo button
        ui.notification_show(
            f"Tweeted '{msg}'",
            action=ui.input_action_button("undo", "Undo?"),
            duration=None,
            id="tweeted",
            type="warning",
            close_button=False,
        )

        # Cancel any existing task if the user clicks tweet twice rapidly
        if waiting_task.get() is not None:
            waiting_task.get().cancel()

        # Create a delayed task (the "runLater" equivalent)
        async def delayed_send():
            try:
                await asyncio.sleep(3)  # Wait for 3 seconds
                print(f"Actually sending tweet: {msg}...")
                ui.notification_remove("tweeted")
                waiting_task.set(None)
            except asyncio.CancelledError:
                # Task was cancelled by the Undo button
                pass

        # Schedule the task in the background
        task = asyncio.create_task(delayed_send())
        waiting_task.set(task)

    @reactive.Effect
    @reactive.event(input.undo)
    def handle_undo():
        task = waiting_task.get()
        if task is not None:
            task.cancel()
            waiting_task.set(None)
            
            # Restore the message and update UI
            ui.notification_show("Tweet retracted", id="tweeted")
            ui.update_text_area("message", value=last_message.get())

app = App(app_ui, server)