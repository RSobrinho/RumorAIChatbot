from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted, AllSlotsReset, ActiveLoop
from rasa_sdk.executor import CollectingDispatcher


class ActionFinalizarSemRumor(Action):
    def name(self) -> Text:
        return "action_finalizar_sem_rumor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="❌ *A conversa foi finalizada, mas nenhum rumor foi criado.*\n"
                 "Caso deseje reportar um rumor, por favor, mande uma nova mensagem. 📩"
        )
        return [AllSlotsReset(), ActiveLoop(None), Restarted()]
