from typing import Any, Text, Dict

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from actions.actions_formulario_principal.validation_utils import is_timeout, deactivate_by_timeout


def validate_afetados(
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
) -> Dict[Text, Any]:
    if is_timeout(slot_value):
        return deactivate_by_timeout()

    tipo_afetado = tracker.get_slot("tipo_afetado")
    valid_options = []
    if tipo_afetado == "Pessoas":
        valid_options = ["Adultos", "Crianças", "Idosos"]
    elif tipo_afetado == "Animais":
        valid_options = ["Animais domésticos", "Animais selvagens", "Animais de produção"]
    elif tipo_afetado == "Meio Ambiente":
        valid_options = ["Poluição", "Desastres naturais", "Não sei"]

    if slot_value in valid_options:
        return {"afetados": slot_value}
    else:
        dispatcher.utter_message(text="⚠️ *Por favor, selecione uma das opções fornecidas.*")
        return {"afetados": None}
