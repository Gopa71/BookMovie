from django.urls import path
from .import views
urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.molly,name='molly'),
    path('hollywood/',views.holly,name='holly'),
    path('bollywood/',views.bolly,name='bolly'),
    path('mdetails/<int:movie_id>',views.mdetails,name='mdetails/'),
    path('hdetails/',views.hdetails,name='hdetails'),
    path('bdetails/',views.bdetails,name='bdetails'),
    
]