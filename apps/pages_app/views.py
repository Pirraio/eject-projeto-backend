from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'pages_app/homepage.html')

#def forum(request):
#   return render(request, 'pages_app/forum.html')

def pais_e_profs(request):
    return render(request, 'pages_app/pais_profs.html')

def videos(request):
    return render(request, 'pages_app/videos.html')
