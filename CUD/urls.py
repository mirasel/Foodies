from django.urls import path
from . import views

app_name = "cud"

urlpatterns =[
    path('',views.addpage, name='Add'),
    path('addplace/',views.addplace,name='place'),
    path('addrestuarant/',views.addrestuarant,name='restuarant'),
    path('addmenu/',views.addmenu,name='menu'),

]
