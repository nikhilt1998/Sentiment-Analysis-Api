from pyramid.view import view_config, view_defaults
from sentiment_api import model
import json

@view_defaults(route_name='sent_json')
class SentimentAPI:
    
    def __init__(self, request):
        self.request = request

        
    @view_config(renderer='json')
    def hello_json(self):

        #get the review from text_review paramater
        text_review = self.request.params.get('text_review', 'No Review')

        #Create an instance of the class Model with text_review
        sent_model=model.Model(text_review)

        #get the sentiment
        sentiment=sent_model.get_sentiment()

        #send json response
        response={"Review": text_review, "Sentiment": sentiment}
        return response