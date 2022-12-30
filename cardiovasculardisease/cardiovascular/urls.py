from django.urls import path
from . import views

urlpatterns = [
    path('', views.prediction, name = 'prediction'),
    path('result', views.final_result, name = 'final_result'),
    path('cardioForm', views.cardioForm, name = 'cardioform'),

]