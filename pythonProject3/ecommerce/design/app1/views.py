from django.shortcuts import render
from app1.models import Team
from app1.models import Place

def home(request):
    p = Place.objects.all()
    t = Team.objects.all()
    return render(request,'home.html',{'p':p,'t':t})
def contact(request):
    return render(request,'contact.html')
def destinations(request):
    return render(request,'destinations.html')
def elements(request):
    return render(request,'elements.html')
def news(request):
    return render(request,'news.html')
# Create your views here.
