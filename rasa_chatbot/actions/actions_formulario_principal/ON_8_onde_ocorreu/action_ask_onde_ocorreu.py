from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskOndeOcorreu(Action):
    def name(self) -> Text:
        return "action_ask_onde_ocorreu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "📍 *Onde ocorreu?*\n\nPor favor, digite o endereço completo."
        dispatcher.utter_message(text=message)
        return []
