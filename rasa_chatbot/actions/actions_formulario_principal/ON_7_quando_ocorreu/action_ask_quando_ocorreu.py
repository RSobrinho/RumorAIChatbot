from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskQuandoOcorreu(Action):
    def name(self) -> Text:
        return "action_ask_quando_ocorreu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("sabe_quando") == "Sim":
            dispatcher.utter_message(
                text="📅 *Por favor, informe a data de quando ocorreu no formato DIA/MÊS/ANO (ex: 15/10/2010).*")
        elif tracker.get_slot("sabe_quando") == "Não":
            dispatcher.utter_message(text="Tudo bem, vamos continuar mesmo assim, ok? 😊")

        return []
