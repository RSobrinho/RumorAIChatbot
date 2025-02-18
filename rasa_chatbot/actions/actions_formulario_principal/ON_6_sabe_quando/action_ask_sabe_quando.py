from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskSabeQuando(Action):
    def name(self) -> Text:
        return "action_ask_sabe_quando"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"title": "👍 Sim", "payload": "Sim"},
            {"title": "👎 Não", "payload": "Não"},
        ]
        message = "📅 *Você sabe quando ocorreu?*\n\nPor favor, selecione uma das opções abaixo:"
        dispatcher.utter_message(text=message, buttons=buttons)
        return []
