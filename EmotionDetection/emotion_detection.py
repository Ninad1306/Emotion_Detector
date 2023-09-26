import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        res = {'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'], 
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'], 
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'], 
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'], 'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
        }
        emotion = max(zip(res.values(), res.keys()))[1]

        return {'anger': res['anger'], 'disgust': res['disgust'],'fear': res['fear'],
         'joy': res['joy'],'sadness': res['sadness'],'dominant_emotion': emotion 
        }
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None,'fear': None, 'joy': None,
        'sadness': None,'dominant_emotion': None 
        }
             
    