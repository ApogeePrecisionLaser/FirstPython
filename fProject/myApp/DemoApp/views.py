from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def demo(request):
    # return HttpResponse("Hello Django Web App")
    return render(request,'DemoApp/login.html')
    # return render(request, 'DemoApp/mainPage.html')


def profile(request):
    # data = request.POST.get('textbox1')
    # context = {'data': data}
    return render(request, 'DemoApp/mainPage.html')

def configuration(request):
    return render(request, 'DemoApp/configuration.html')

def status(request):
    return render(request, 'DemoApp/status.html')

def satellite_info(request):
    return render(request, 'DemoApp/satellite_info.html')

def data_recode(request):
    return render(request, 'DemoApp/data_recode.html')

def internet(request):
    return render(request, 'DemoApp/internet.html')

def io_config(request):
    return render(request, 'DemoApp/io_config.html')

def forward_upgrade(request):
    return render(request, 'DemoApp/forward_upgrade.html')

def user_management(request):
    return render(request, 'DemoApp/user_management.html')
