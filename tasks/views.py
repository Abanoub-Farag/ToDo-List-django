from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView, UpdateView

class TaskMixin(LoginRequiredMixin):
    model = Task
    success_url = "/"
    pk_url_kwarg = 'id'


class HomePageView(TaskMixin, ListView):

    template_name = "home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CreateTaskView(TaskMixin, CreateView):
    
    form_class = TaskForm
    template_name = "create_task.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteTaskView(TaskMixin, UserPassesTestMixin, DeleteView):

    template_name = "task_confirm_deletion.html"
    raise_exception = True

    # def test_func(self):
    #     task = self.get_object()
    #     return task.user == self.request.user

    def get_queryset(self):
        return self.model.objects.all()

    def test_func(self):
        return self.get_object().user == self.request.user


class UpdateTaskView(TaskMixin, UserPassesTestMixin, UpdateView):

    form_class = TaskForm
    template_name = "update_task.html"
    raise_exception = True

    def test_func(self):
        return self.get_object().user == self.request.user