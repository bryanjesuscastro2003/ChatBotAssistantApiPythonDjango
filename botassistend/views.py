import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai.bot import *

def welcome(request):
    return HttpResponse("App developed by Bryan Jesus")

"""
body
{
      question : "user question"
}
"""

@api_view(["POST"])
def botAssistant(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question = body["question"]
        pred = predict_class(question.lower()) 
        response = get_response(pred, intents)
        return Response({"ok": True, "message": "Bot running ok", "data": response})
    except Exception as e:
        return Response({"ok": False, "message": "Server error try again later", "data": []})
