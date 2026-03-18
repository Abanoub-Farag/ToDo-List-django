from django.urls import path
from .views import (
    HomePageView, create_task_view,
    DeleteTaskView, update_task_view
)


urlpatterns = [
    path("delete_task/<int:id>/", DeleteTaskView.as_view(), name="delete_task"),
    path("update_task/<int:id>/", update_task_view, name="update_task"),
    path("create_task/", create_task_view, name="create_task"),
    path("", HomePageView.as_view(), name="home")
]