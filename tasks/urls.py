from django.urls import path
from .views import (
    HomePageView, CreateTaskView,
    DeleteTaskView, UpdateTaskView
)


urlpatterns = [
    path("delete_task/<int:id>/", DeleteTaskView.as_view(), name="delete_task"),
    path("update_task/<int:id>/", UpdateTaskView.as_view(), name="update_task"),
    path("create_task/", CreateTaskView.as_view(), name="create_task"),
    path("", HomePageView.as_view(), name="home")
]