def post(self, request):

        """Returns the result of detect intent with texts as inputs.
        Using the same `session_id` between requests allows continuation
        of the conversaion."""
        # GOOGLE_APPLICATION_CREDENTIALS = 'file.json'

        texts = request.data["text"]

        project_id = "YOUR-PROGECT-ID"
        session_id = str(uuid.uuid4())
        language_code = "en-US"
        texts_ = list()
        texts_.append(texts)
        try:
            session_client = dialogflow.SessionsClient()
            session = session_client.session_path(project_id, session_id)
            for text in texts_:
                text_input = dialogflow.types.TextInput(
                    text=text, language_code=language_code)
                query_input = dialogflow.types.QueryInput(text=text_input)
                response = session_client.detect_intent(
                    session=session, query_input=query_input)
                """ Dialogflow return answer HERE"""
            key_words = list()
            for i in response.query_result.fulfillment_text.split(', '):
                key_words.append(i)

# THIS CODE WORKS FOR CALL INTENTS FROM DIALOGFLOW 
# for request to *dialogflow* you need :
# `project_id`, `session_id`
