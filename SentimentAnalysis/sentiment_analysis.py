import requests
import json
#https://developer.ibm.com/apis/catalog/embeddableai--watson-natural-language-processing-apis/api/API--embeddableai--watson-natural-language-processing-apis#SentimentPredict
def sentiment_analyzer(text_to_analyse):
        """"creating the sentiment analysis application"""
        #url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
        url = #https://localhost:8080/v1/watson.runtime.nlp.v1/NlpService/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
        header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
        myobj = {"raw_document": { "text": text_to_analyse } }
        
        response = requests.post(url, json = myobj, headers = header)
       
        # format response
        formatted_response = json.loads(response.text)
        if response.status_code == 200:
        #get value of dictionary keys label and score
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        else:
            label = None
            score = None
        #return response
        #return formatted_response
        # return dictionary
        return {'label':label, 'score':score}
    