import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=myobj, headers=headers)
    
    return response.text

def emotion_predictor(text_to_analyze):
    raw_response = emotion_detector(text_to_analyze)
    formatted_response = json.loads(raw_response)
    
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
