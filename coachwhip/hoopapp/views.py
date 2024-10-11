from django.shortcuts import render

# Create your views here.
def hoopview(request):
    return render(request, 'index.html')

def halloumi(request):
    return render(request, 'halloumi.html')
