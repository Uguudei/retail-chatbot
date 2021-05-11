from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from actions import config
from pprint import pprint
import json


class ActionChitChat(Action):
    def name(self) -> Text:
        return "action_chitchat"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,  # Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        latest_message = tracker.latest_message
        latest_intent = tracker.get_intent_of_latest_message()
        retrieval_intents = latest_message['response_selector']['all_retrieval_intents']
        if latest_intent in retrieval_intents:
            retrieval_intent = latest_message['response_selector'][latest_intent]
            response_ranking = retrieval_intent['ranking']
            confidence = retrieval_intent['ranking'][0]['confidence']
            utter_action = retrieval_intent['response']['utter_action']
            if confidence > 0.7:
                dispatcher.utter_message(response=utter_action)
                dispatcher.utter_message(text=f"Selected response: {utter_action}")
                pretty_response_ranking = json.dumps(response_ranking, indent=2)
                dispatcher.utter_message(text=f'Responses:\n{pretty_response_ranking}')
            else:
                dispatcher.utter_message(text="confidence below 0.7")
        return []
