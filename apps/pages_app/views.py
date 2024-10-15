from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages_app/homepage.html')

def forum(request):
    return render(request, 'pages_app/forum.html')
