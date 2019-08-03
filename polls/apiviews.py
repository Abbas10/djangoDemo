from datetime import datetime

from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Question


@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        return HttpResponse("Not Implemented")
    elif request.method == 'POST':
        question_text = request.data['question_text']
        pub_date = datetime.strptime(request.data['pub_date'], '%Y-%m-%d')
        Question.objects.create(question_text=question_text, pub_date=pub_date)
        return HttpResponse("Question created", status=201)
