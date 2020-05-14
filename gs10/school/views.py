from django.shortcuts import render

# Create your views here.
def student_name(request):
    return render(request, 'school.htm')