from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tours(request):
    return render(request, 'tours.html')