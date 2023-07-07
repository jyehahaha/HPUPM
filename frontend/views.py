from django.shortcuts import render

# Create your views here.
def IndexView(request):
    context = {

    }
    return render(request,'frontend/index.html', context)

def LoginView(request):
    context = {

    }
    return render(request,'frontend/login.html', context)

def DashboardView(request):
    context = {

    }
    return render(request,'frontend/dashboard.html', context)
