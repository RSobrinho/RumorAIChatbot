from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPerguntaAfetado(Action):
    def name(self) -> Text:
        return "action_ask_afetados"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tipo_afetado = tracker.get_slot("tipo_afetado")
        message = ""
        buttons = []

        if tipo_afetado == "Pessoas":
            buttons = [
                {"title": "👨 Adultos", "payload": "Adultos"},
                {"title": "👶 Crianças", "payload": "Crianças"},
                {"title": "👵 Idosos", "payload": "Idosos"},
            ]
            message = "Que tipo de pessoa?"
        elif tipo_afetado == "Animais":
            buttons = [
                {"title": "🐶 Domésticos", "payload": "Animais domésticos"},
                {"title": "🐮 Produção", "payload": "Animais de produção"},
                {"title": "🐒 Selvagens", "payload": "Animais selvagens"},
            ]
            message = (
                "Que tipo de animal?\n\n"
                "Exemplos:\n"
                "- Animais Domésticos (Cachorro, Gato, etc.)\n"
                "- Animais de Produção (Cavalo, Galinha, Porco, Vaca, etc.)\n"
                "- Animais Selvagens (Aves, Capivara, Escorpião, Macaco, Morcego, etc.)"
            )
        elif tipo_afetado == "Meio Ambiente":
            buttons = [
                {"title": "🌫️ Poluição", "payload": "Poluição"},
                {"title": "🌪️ Desastres naturais", "payload": "Desastres naturais"},
                {"title": "❓ Não sei", "payload": "Não sei"},
            ]
            message = "Que tipo de impacto ambiental?"

        dispatcher.utter_message(text=f"📋 *{message}*\n\nEscolha uma das opções abaixo:", buttons=buttons)
        return []

