from django.shortcuts import render
from .models import Movies

# Create your views here.
# def home(req):
#     return render(req,'index.html')
def molly(req):
    obj=Movies.objects.all
    return render(req,'molly.html',{'movies':obj})
def holly(req):
    return render(req,'holly.html')
def bolly(req):
    return render(req,'bolly.html')
def mdetails(req,movie_id):
    
    data=Movies.objects.get(id=movie_id)
    return render(req,'Mdetails.html',{'data':data})
def hdetails(req):
    return render(req,'hdetails.html')
def bdetails(req):
    return render(req,'bdetails.html')