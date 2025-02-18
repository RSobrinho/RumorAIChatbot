from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSaudaRumorAIChatbot(Action):
    def name(self) -> Text:
        return "action_sauda_rumor_ai_chatbot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"title": "📢 Reportar um rumor", "payload": "/Rumor"},
            {"title": "🔍 Outros", "payload": "/outros"},
            {"title": "❓ Dúvidas", "payload": "/para_que_serve"}
        ]

        dispatcher.utter_message(
            text=(
                "*Olá! Bem-vindo(a) ao RumorAIChatbot!* 😊"
                "\n*Como podemos ajudar você hoje?*"
                "\n\n📢 *Informar um rumor* - Faça o envio de um rumor"
                "\n🔍 *Outros* - Deseja realizar alguma outra ação que não corresponde às alternativas acima."
                "\n❓ *Dúvidas* - Esclareça suas dúvidas sobre o objetivo do RumorAIChatbot."
                "\n\n*Clique em uma das opções abaixo:* 👇"
            ),
            buttons=buttons
        )

        return []
