from datetime import datetime, timedelta
from rasa_sdk import Action
from rasa_sdk.events import ReminderScheduled


class ActionSetReminder(Action):
    def name(self):
        return "action_set_reminder"

    async def run(self, dispatcher, tracker, domain):
        date_time = datetime.now() + timedelta(minutes=20)
        print(f"Setting reminder for: {date_time}")

        reminder = ReminderScheduled(
            intent_name="EXTERNAL_reminder",
            trigger_date_time=date_time,
            entities=[],
            name="user_inactivity",
            kill_on_user_message=False
        )

        print(f"Reminder scheduled: {reminder}")

        return [reminder]