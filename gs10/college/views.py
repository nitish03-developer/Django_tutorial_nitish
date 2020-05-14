from django.shortcuts import render

# Create your views here.
def college_name(request):
    return render(request, 'college.htm')