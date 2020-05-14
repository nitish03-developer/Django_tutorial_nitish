from django.shortcuts import render

# Create your views here.

def chinu_dj(request):
    return render(request, 'Chinu/chinuone.htm')

def chinu_py(request):
    return render(request, 'Chinu/chinutwo.htm')