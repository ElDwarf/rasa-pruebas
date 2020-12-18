# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_search_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        #Get Input from user
        limit = tracker.latest_message['text']
        print(limit)
        df = pd.read_csv("./dataset/copy_data_credit.csv")
        list_ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        value_random = random.choice(list_ids)
        df.iloc[value_random,'USER_TEL'] = limit
        df.to_csv("./dataset/copy_data_credit.csv")
        dispatcher.utter_message(text="Este es tu credit id: {}".format(str(df['CRD_CREDIT_ID'][value_random])))
        return []