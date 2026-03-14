from django.urls import path
from .views import HomePageView, TasksPageView


urlpatterns = [
    path("create_task/", ),
    path("tasks/", TasksPageView.as_view()),
    path("", HomePageView.as_view())
]