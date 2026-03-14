from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


from .models import tasks

def home_page_view(request):
    objects = tasks.objects.all()
    return render(request, "home.html", context={"tasks" : objects})


def create_task_view(request):
    if request.method == "POST":
        data = request.POST.get("title")
        tasks.objects.create(
            title = data
        )

        return redirect("home")
    
    return render(request, "create_task.html")


def delete_task(request, id):
    task = get_object_or_404(tasks, id=id)
    task.delete()
    return redirect("/")