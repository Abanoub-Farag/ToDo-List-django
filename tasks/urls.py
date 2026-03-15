from django.urls import path
from .views import (
    home_page_view, create_task_view,
    delete_task, update_task_view
)


urlpatterns = [
    path("delete_task/<int:id>/", delete_task, name="delete_task"),
    path("update_task/<int:id>", update_task_view, name="update_task"),
    path("create_task/", create_task_view, name="create_task"),
    path("", home_page_view, name="home")
]