from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionExplicarDuvidas(Action):
    def name(self) -> Text:
        return "action_explicar_duvidas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mensagem1 = (
            "📝 *O que é o RumorAIChatbot? (finish)*\n"
        )

        mensagem2 = (
            "📢 *O que é um rumor?*\n"
            "Um rumor é uma informação que circula sem confirmação e com origem incerta. "
        )

        mensagem3 = (
            "🤖 *Como o chatbot ajuda?*\n"
            "Este chatbot foi desenvolvido para facilitar a detecção e comunicação."
            "Ele pode ajudar a reportar rumores, facilitando a comunicação da sociedade com um orgão de saúde"
            "Estou aqui para encaminhar seu atendimento da melhor forma possível. 😊"
        )

        dispatcher.utter_message(text=mensagem1)
        dispatcher.utter_message(text=mensagem2)
        dispatcher.utter_message(text=mensagem3)

        return []
