from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.htm')

def fees_python(request):
    return render(request, 'fees/feestwo.htm')

