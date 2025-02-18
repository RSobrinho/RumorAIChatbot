from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


class ActionBotNaoEntendeu(Action):
    def name(self) -> Text:
        return "action_bot_nao_entendeu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="😕 *Desculpe, não entendi.*\n"
                                      "Pode repetir, por favor? 🙏")
        return [UserUtteranceReverted()]
