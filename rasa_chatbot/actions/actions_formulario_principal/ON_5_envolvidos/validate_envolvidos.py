from typing import Any, Text, Dict

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from actions.actions_formulario_principal.validation_utils import deactivate_by_timeout, is_timeout


def validate_envolvidos(
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
) -> Dict[Text, Any]:
    if is_timeout(slot_value):
        return deactivate_by_timeout()

    if slot_value.isdigit():
        return {"envolvidos": int(slot_value)}
    else:
        dispatcher.utter_message(text="⚠️ *Por favor, insira somente o número.*\nEx: 3")
        return {"envolvidos": None}
