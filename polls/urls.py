from django.urls import path

from . import views
from . import apiviews

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    # the 'name' value as called by the {% url %} template tag
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    ################################ API routes #########################

    # ex: POST      /polls/questions/
    # ex: GET       /polls/questions/
    path('questions/', apiviews.questions_view, name='questions_view'),

    # ex: GET       /polls/questions/4
    # ex: PATCH     /polls/questions/4
    # ex: DELETE    /polls/questions/4
    path('questions/<int:question_id>',
         apiviews.question_detail_view, name='question_detail_view'),

    # ex: POST      /polls/questions/4
    path('questions/<int:question_id>/choices/',
         apiviews.choices_view, name='choices_view')

]
