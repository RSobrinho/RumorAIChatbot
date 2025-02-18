from typing import Any, Text, Dict

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from actions.actions_formulario_principal.validation_utils import is_timeout, deactivate_by_timeout


def validate_sabe_quando(
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
) -> Dict[Text, Any]:
    if is_timeout(slot_value):
        return deactivate_by_timeout()

    valid_options = ["Sim", "Não"]
    if slot_value in valid_options:
        return {"sabe_quando": slot_value}
    else:
        dispatcher.utter_message(text="⚠️ *Por favor, selecione uma das opções fornecidas: Sim ou Não.*")
        return {"sabe_quando": None}
