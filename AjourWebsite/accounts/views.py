from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def indexView(request):
    return render(request, 'index.html')


@login_required(login_url='login_url')
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url="login_url")
def mlPrediction(request):
    param1 = request.POST.get("degreesValue")
    param2 = request.POST.get("weatherValue")
    prediction = "HEJJJE " + param1 + param2

    return render(request, "dashboard.html", {"data1": prediction})
