from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskTipoAfetado(Action):
    def name(self) -> Text:
        return "action_ask_tipo_afetado"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"title": "👤 Pessoas", "payload": "Pessoas"},
            {"title": "🐾 Animais", "payload": "Animais"},
            {"title": "🌳 Meio Ambiente", "payload": "Meio Ambiente"},
        ]
        message = "📋 *Quem foram os afetados?*\n\nEscolha uma das opções abaixo:"
        dispatcher.utter_message(text=message, buttons=buttons)
        return []
