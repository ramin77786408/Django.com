from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='home'),
    path('learning_django/', views.DjangoLearningView.as_view(), name='learning_django'),
]