from django.shortcuts import render,redirect
from .models import Movies
from .forms import MovieForm


def molly(req):
    obj=Movies.objects.all
    return render(req,'molly.html',{'movies':obj})
def mdetails(req,movie_id): 
    data=Movies.objects.get(id=movie_id)
    return render(req,'Mdetails.html',{'data':data})


def registermovie(req,):

    if req.method=='POST':
        name=req.POST.get('name')
        rate=req.POST.get('rate')
        screen=req.POST.get('screen')
        language=req.POST.get('language')
        date_dur=req.POST.get('date_dur')
        photo=req.FILES['photo']
        bgphoto=req.FILES['bgphoto']

        movie=Movies(name=name,rate=rate,screen=screen,language=language,date_dur=date_dur,photo=photo,bgphoto=bgphoto)
        movie.save()

        return redirect('/')





    return render(req,'regmovie.html')

def delete(req,detail_id):
    if req.method=='POST':
      data=Movies.objects.get(id=detail_id) 
      data.delete()
      return redirect('/')
   

    return render(req,'delete.html')

def update(req,update_id):
    movie=Movies.objects.get(id=update_id)
    form=MovieForm(req.POST or None,req.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(req,'edit.html',{'form':form,'movie':movie})