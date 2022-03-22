from django.urls import path
from .models import *
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz')
]