from django.shortcuts import render, redirect

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