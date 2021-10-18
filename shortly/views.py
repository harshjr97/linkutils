from django.shortcuts import render
import pyshorteners
# Create your views here.

def home(request):
    s = pyshorteners.Shortener()
    shortlink = ""
    if request.method == "POST":
        link = request.POST['link']
        link.replace("https://","")
        link.replace("http://","")
        shortlink = s.tinyurl.short(link)
    
    context = {'shortlink': shortlink}

    return render(request, 'index.html', context)

    