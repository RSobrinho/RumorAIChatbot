from typing import Any, Text, Dict
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from datetime import datetime

from actions.actions_formulario_principal.validation_utils import is_timeout, deactivate_by_timeout


def validate_quando_ocorreu(
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
) -> Dict[Text, Any]:
    if is_timeout(slot_value):
        return deactivate_by_timeout()

    sabe_quando = tracker.get_slot("sabe_quando")
    # Se o usuário não sabe quando ocorreu, não precisa validar a data
    if sabe_quando == "Sim":
        # Tenta analisar a data no formato correto
        try:
            datetime.strptime(slot_value, "%d/%m/%Y")
            return {"quando_ocorreu": slot_value}
        except ValueError:
            try:
                # Tenta converter a data para o formato correto
                converted_date = datetime.strptime(slot_value, "%d-%m-%Y").strftime("%d/%m/%Y")
                return {"quando_ocorreu": converted_date}
            except ValueError:
                dispatcher.utter_message(text="⚠️ *Por favor, insira uma data válida no formato DIA/MÊS/ANO (ex: 15/10/2010).*")
                return {"quando_ocorreu": None}
    else:
        return {"quando_ocorreu": slot_value}
