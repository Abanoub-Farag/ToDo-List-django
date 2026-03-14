from django.urls import path
from .views import home_page_view, create_task_view


urlpatterns = [
    path("create_task/", create_task_view, name="create_task"),
    path("", home_page_view, name="home")
]