from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class ActionFinalizarFormulario(Action):
    def name(self) -> Text:
        return "action_finalizar_formulario"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        was_timeout = tracker.get_slot('was_timeout')

        if was_timeout:
            dispatcher.utter_message(text="⏳ *Formulário incompleto devido a tempo excedido.*")
            return [FollowupAction(name='action_finalizar_sem_rumor')]

        return [FollowupAction(name='action_finalizar_com_rumor')]
