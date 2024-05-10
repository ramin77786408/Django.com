from django.shortcuts import render,get_object_or_404
from django.views import generic




def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, "home/Django_Tutorial.html")

class DjangoLearningView(generic.TemplateView):
    template_name = "home/django_intro.html"