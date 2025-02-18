from rasa_sdk import Action
from rasa_sdk.events import ReminderCancelled


class ActionCancelReminder(Action):
    def name(self):
        return "action_cancel_reminder"

    async def run(self, dispatcher, tracker, domain):
        reminder = ReminderCancelled(
            name="user_inactivity"
        )

        print(f"Reminder cancelled for user: {tracker.sender_id}")

        return [reminder]