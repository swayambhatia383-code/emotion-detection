import json
import requests


def emotion_detector(text_to_analyse):
    """Analyzes the input text for emotion using the Watson NLP Emotion Detection service.

    Args:
        text_to_analyse(str): The text string to be analyzed.

    Returns:
        str: Raw response text from the Watson NLP Emotion Detection API.
    """
    # Service endpoint URL and required model metadata headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Request body structure expected by the Watson NLP API
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Send HTTP POST request to Watson NLP API
    response = requests.post(url, json=myobj, headers=headers)

    # Return the raw response text directly as requested by the task 2 rubric
    return response.text
