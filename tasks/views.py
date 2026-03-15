from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


from .models import Task

def home_page_view(request):
    objects = Task.objects.all()
    context = {"tasks" : objects}
    return render(request, "home.html", context)


def create_task_view(request):
    if request.method == "POST":
        data = request.POST
        Task.objects.create(
            title = data.get("title"),
            description = data.get("description")
        )

        return redirect("home")
    
    return render(request, "create_task.html")


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("/")


def update_task_view(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        data = request.POST
        task.title = data.get("title")
        task.description = data.get("description")
        task.save()
        return redirect("/")

    context = {"task" : task}
    return render(request, "update_task.html", context)