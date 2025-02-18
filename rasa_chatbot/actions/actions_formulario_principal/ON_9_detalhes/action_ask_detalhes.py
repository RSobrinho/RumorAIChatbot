from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskDetalhes(Action):
    def name(self) -> Text:
        return "action_ask_detalhes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "📝 *Deseja informar mais detalhes?*\n\nSe sim, descreva-os abaixo."
        dispatcher.utter_message(text=message)
        return []
