from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionExplicarLimitacoes(Action):
    def name(self) -> Text:
        return "action_explicar_limitacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text=(
                "⚠️ *Limitações do Chatbot*\n"
                "No momento, este chatbot está limitado apenas ao envio de informações relacionadas a rumores "
                "(informações que circulam sem confirmação e com origem incerta). "
                "Se sua necessidade não estiver relacionada a este contexto, pode ser que você esteja contatando "
                "o serviço errado. "
                "\n\n📞 Se precisar de mais assistência, pode contatar a *Ouvidoria SUS* pelo número *0800 314 9955*."
            )
        )
        return []
