from typing import Any, Text, Dict
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from actions.actions_formulario_principal.ON_2_tipo_afetado.validate_tipo_afetado import validate_tipo_afetado
from actions.actions_formulario_principal.ON_3_descricao.validate_descricao import validate_descricao
from actions.actions_formulario_principal.ON_4_afetados.validate_afetados import validate_afetados
from actions.actions_formulario_principal.ON_5_envolvidos.validate_envolvidos import validate_envolvidos
from actions.actions_formulario_principal.ON_6_sabe_quando.validate_sabe_quando import validate_sabe_quando
from actions.actions_formulario_principal.ON_7_quando_ocorreu.validate_quando_ocorreu import validate_quando_ocorreu
from actions.actions_formulario_principal.ON_8_onde_ocorreu.validate_onde_ocorreu import validate_onde_ocorreu
from actions.actions_formulario_principal.ON_9_detalhes.validate_detalhes import validate_detalhes


class ValidateRumoresForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_rumores_form"

    def validate_tipo_afetado(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_tipo_afetado(slot_value, dispatcher, tracker, domain)

    def validate_descricao(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_descricao(slot_value, dispatcher, tracker, domain)

    def validate_afetados(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_afetados(slot_value, dispatcher, tracker, domain)

    def validate_envolvidos(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_envolvidos(slot_value, dispatcher, tracker, domain)

    def validate_sabe_quando(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_sabe_quando(slot_value, dispatcher, tracker, domain)

    def validate_quando_ocorreu(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_quando_ocorreu(slot_value, dispatcher, tracker, domain)

    def validate_onde_ocorreu(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_onde_ocorreu(slot_value, dispatcher, tracker, domain)

    def validate_detalhes(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        return validate_detalhes(slot_value, dispatcher, tracker, domain)
