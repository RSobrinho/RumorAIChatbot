from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import time


class ActionSetStartDate(Action):
    def name(self) -> Text:
        return "action_set_start_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Verificar se o slot "start_date" já está definido
        if tracker.get_slot("start_date") is None:
            # Armazenar o timestamp de início na slot "start_date"
            start_date = time.time()
            print("Start Date:", start_date)
            return [SlotSet("start_date", start_date)]
        else:
            # Não atualizar o valor da slot "start_date" se já estiver definido
            return []