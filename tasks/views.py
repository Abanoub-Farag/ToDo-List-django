from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from django.views import View

# @login_required
# def home_page_view(request):
#     objects = Task.objects.filter(user=request.user)
#     context = {"tasks" : objects}
#     return render(request, "home.html", context)

class HomePageView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, "home.html", {"tasks" : Task.objects.filter(user=request.user)})

@login_required
def create_task_view(request):
    if request.method == "POST":
        data = request.POST
        Task.objects.create(
            user=request.user,
            title = data.get("title"),
            description = data.get("description")
        )

        return redirect("home")
    
    return render(request, "create_task.html")

# @login_required
# def delete_task(request, id):
#     task = get_object_or_404(Task, id=id, user=request.user)
#     task.delete()
#     return redirect("/")


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/"
    template_name = "task_confirm_deletion.html"
    pk_url_kwarg = 'id'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

@login_required
def update_task_view(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == "POST":
        data = request.POST
        task.title = data.get("title")
        task.description = data.get("description")
        task.save()
        return redirect("/")

    context = {"task" : task}
    return render(request, "update_task.html", context)
