from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import time


class ActionSetEndDate(Action):
    def name(self) -> Text:
        return "action_set_end_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Verificar se o slot "end_date" já está definido
        if tracker.get_slot("end_date") is None:
            # Armazenar o timestamp de início na slot "end_date"
            end_date = time.time()
            print("End Date:", end_date)
            return [SlotSet("end_date", end_date)]
        else:
            # Não atualizar o valor da slot "start_date" se já estiver definido
            return []
