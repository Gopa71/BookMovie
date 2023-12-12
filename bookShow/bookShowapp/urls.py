from django.urls import path
from .import views

app_name='bookmyshow'
urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.molly,name='molly'),
    path('mdetails/<int:movie_id>',views.mdetails,name='mdetails/'),
    


    path('registermovie/',views.registermovie,name='regmovie'),
    path('delete/<int:detail_id>',views.delete,name='delete')
    
]