from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPerguntaDescricao(Action):
    def name(self) -> Text:
        return "action_ask_descricao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tipo_afetado = tracker.get_slot("tipo_afetado")
        message = ""
        buttons = []

        if tipo_afetado == "Pessoas":
            buttons = [
                {"title": "🤒 Sintomas parecidos", "payload": "Doentes com sintomas parecidos"},
                {"title": "🦠 Sintomas novos/raros", "payload": "Doentes com sintomas novos/raros"},
                {"title": "⚰️ Mortes inexplicadas", "payload": "Pessoas com mortes inexplicadas"},
            ]
            message = "Marque a opção que melhor descreve o que ocorreu com as pessoas:"
        elif tipo_afetado == "Animais":
            buttons = [
                {"title": "🤒 Sintomas parecidos", "payload": "Animais sintomas parecidos"},
                {"title": "🦠 Sintomas novos/raros", "payload": "Animais sintomas novos"},
                {"title": "⚰️ Mortes inexplicadas", "payload": "Mortes inexplicadas"},
            ]
            message = "Marque a opção que melhor descreve o que ocorreu com os animais:"
        elif tipo_afetado == "Meio Ambiente":
            buttons = [
                {"title": "👤 Pessoas afetadas", "payload": "Pessoas afetadas fenômenos ambientais"},
                {"title": "🐾 Animais afetados", "payload": "Animais afetados fenômenos ambientais"},
                {"title": "💧 Água anormal", "payload": "Fonte de agua com cor ou odor anormal"}
            ]
            message = "Marque a opção que melhor descreve o que ocorreu com o meio ambiente:"

        dispatcher.utter_message(text=f"📋 *{message}*\n\nEscolha uma das opções abaixo:", buttons=buttons)
        return []
