from fuzzywuzzy import process
import json
import os
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from typing import Any, Text, Dict, List


class ActionFetchInfo(Action):
    def name(self) -> Text:
        return "action_fetch_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Load knowledge base
        file_path = "actions/knowledge_base.json"
        if not os.path.exists(file_path):
            dispatcher.utter_message(text=f"Error: File '{file_path}' not found.")
            return []

        try:
            with open(file_path, "r") as file:
                knowledge_base = json.load(file)
        except Exception as e:
            dispatcher.utter_message(text=f"Error loading JSON: {e}")
            return []

        user_query = tracker.latest_message.get("text").lower()

        # Debug: Print user query
        print(f"User Query: {user_query}")

        # Check for specific keywords and respond accordingly
        if "cost" in user_query or "price" in user_query:
            response = knowledge_base["birth_certificate"].get("cost", "Sorry, I couldn't find the cost information.")
            dispatcher.utter_message(text=f"The cost of a birth certificate is: {response}")

        elif "documents" in user_query or "required" in user_query or "need" in user_query:
            response = knowledge_base["birth_certificate"].get("documents_needed",
                                                               "Sorry, I couldn't find the document information.")
            dispatcher.utter_message(text=f"To apply for a birth certificate, you need: {response}")

        elif "apply" in user_query or "where" in user_query or "apply for" in user_query:
            response = knowledge_base["birth_certificate"].get("where_to_apply",
                                                               "Sorry, I couldn't find the application process information.")
            dispatcher.utter_message(text=f"You can apply for a birth certificate at: {response}")

        elif "issuing authority" in user_query or "who issues" in user_query or "who provides" in user_query:
            response = knowledge_base["birth_certificate"].get("issuing_authority",
                                                               "Sorry, I couldn't find the issuing authority information.")
            dispatcher.utter_message(text=f"The issuing authority for birth certificates is: {response}")

        elif "lost certificate" in user_query or "duplicate" in user_query or "lost" in user_query:
            response = knowledge_base["birth_certificate"].get("lost_certificate",
                                                               "Sorry, I couldn't find the information on how to apply for a lost certificate.")
            dispatcher.utter_message(
                text=f"If you have lost your birth certificate, you can apply for a duplicate at: {response}")

        else:
            # Default response if no specific keyword matches
            response = knowledge_base["birth_certificate"].get("definition",
                                                               "Sorry, I couldn't find specific information on that topic.")
            dispatcher.utter_message(text=f"A birth certificate is: {response}")

        return []
