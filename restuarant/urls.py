from django.urls import path
from . import views

app_name = "restuarant"

urlpatterns =[
    path('',views.homepage,name='Home'),
    path('<int:r_id>/menu/',views._menu,name='Menu'),
    path('rateit/',views.rateit,name='Rateit'),
    path('<int:rid>/<int:menuid>/delete/',views.delete,name='delete'),
    path('edit/',views.edit,name='edit'),

]
