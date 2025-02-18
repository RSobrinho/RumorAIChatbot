from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted, AllSlotsReset, ActiveLoop
from rasa_sdk.executor import CollectingDispatcher
import requests
import datetime


class ActionFinalizarComRumor(Action):
    def name(self) -> Text:
        return "action_finalizar_com_rumor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extrair informações do tracker
        sender_id, start_date, end_date, tipo_afetado, descricao, envolvidos, afetados, sabe_quando, quando_ocorreu, onde_ocorreu, detalhes = self.extract_info(
            tracker)

        # Enviar dados para o backend
        return self.send_data_to_backend(dispatcher, sender_id, start_date, end_date, tipo_afetado, descricao,
                                         envolvidos, afetados, sabe_quando, quando_ocorreu, onde_ocorreu, detalhes)

    def extract_info(self, tracker):
        sender_id = tracker.sender_id
        start_date = tracker.get_slot("start_date")
        end_date = tracker.get_slot("end_date")

        # Converter os timestamps Unix para objetos datetime
        start_datetime = datetime.datetime.fromtimestamp(start_date)
        end_datetime = datetime.datetime.fromtimestamp(end_date)

        # Formatá-los como strings
        start_date_str = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
        end_date_str = end_datetime.strftime('%Y-%m-%d %H:%M:%S')

        tipo_afetado = tracker.get_slot("tipo_afetado")
        descricao = tracker.get_slot("descricao")
        afetados = tracker.get_slot("afetados")
        envolvidos = tracker.get_slot("envolvidos")
        sabe_quando = tracker.get_slot("sabe_quando")
        quando_ocorreu = tracker.get_slot("quando_ocorreu")
        onde_ocorreu = tracker.get_slot("onde_ocorreu")
        detalhes = tracker.get_slot("detalhes")

        return sender_id, start_date_str, end_date_str, tipo_afetado, descricao, envolvidos, afetados, sabe_quando, quando_ocorreu, onde_ocorreu, detalhes

    def send_data_to_backend(self, dispatcher, sender_id, start_date, end_date, tipo_afetado, descricao, envolvidos,
                             afetados, sabe_quando, quando_ocorreu, onde_ocorreu, detalhes):
        # Enviar os dados para o backend
        url = "https://rumoraichatbot-backend.up.railway.app/api/v1/rumor"
        data = {
            "senderNumber": sender_id,
            "startDate": start_date,
            "endDate": end_date,
            "senderAnswers": {
                "tipo_afetado": tipo_afetado,
                "descricao": descricao,
                "envolvidos": envolvidos,
                "afetados": afetados,
                "sabe_quando": sabe_quando,
                "quando_ocorreu": quando_ocorreu,
                "onde_ocorreu": onde_ocorreu,
                "detalhes": detalhes
            }
        }
        response = requests.post(url, json=data)

        if response.status_code == 201:
            dispatcher.utter_message("✅ *Seu rumor foi enviado com sucesso!* O RumorAIChatbot agradece seu contato! 🙏")
        else:
            dispatcher.utter_message(
                "⚠️ *Infelizmente não foi possível contatar o nosso servidor*. Por favor, tente novamente mais tarde. 🙁")
        return [AllSlotsReset(), ActiveLoop(None), Restarted()]
