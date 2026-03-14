from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import tasks

class HomePageView(TemplateView):
    template_name = "home.html"


class TasksPageView(TemplateView):
    objects = tasks.objects.all()

    def get(self, request):
        return render(request, "tasks.html", context={'tasks': self.objects})
    

def create_task_page_view(request):
    