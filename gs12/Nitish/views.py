from django.shortcuts import render

# Create your views here.

def nitish_dj(request):
    return render(request, 'Nitish/nitishone.htm')

def nitish_py(request):
    return render(request, 'Nitish/nitishtwo.htm')