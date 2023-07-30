from django.shortcuts import render


from movies.models import Movies
from movies.forms import Movieform
from django.views.generic import ListView
# from django.db.models import Q

# def home(request):
#     m = Movies.objects.all()
#     return render(request, 'home.html',{'m':m})

class movielistview(Listview):
    model=Movies
    template_name="home.html"
    context_objet_name="m"
def addfilm(request):
    if (request.method == "POST"):
        t = request.POST['t']
        y = request.POST['y']
        r = request.POST['r']
        d = request.POST['d']
        i = request.FILES['i']
        m = Movies.objects.create(title=t, year=y, rating=r, desc=d, img=i)
        m.save()
        return home(request)
    return render(request,'addfilm.html')

def viewdetails(request,p):
    m = Movies.objects.get(id=p)
    return render(request,'viewdetails.html',{'m':m})

def deletemovie(request,p):

    m = Movies.objects.get(id=p)
    m.delete()
    return home(request)

def editmovie(request,p):
    m = Movies.objects.get(id=p)
    form = Movieform(instance=m)
    if (request.method == "POST"):
        form = Movieform(request.POST,request.FILES,instance=m)

        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'editmovie.html', {'form': form})