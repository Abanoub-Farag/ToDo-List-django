from django.urls import path
from .views import home_page_view, create_task_view, delete_task


urlpatterns = [
    path("delete_task/<id>/", delete_task, name="delete_task"),
    path("create_task/", create_task_view, name="create_task"),
    path("", home_page_view, name="home")
]