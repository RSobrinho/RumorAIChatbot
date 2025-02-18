from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskEnvolvidos(Action):
    def name(self) -> Text:
        return "action_ask_envolvidos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "👥 *Quantas pessoas estão envolvidas?*\n\nPor favor, insira somente o número. Ex: 3"
        dispatcher.utter_message(text=message)
        return []
