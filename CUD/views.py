from django.shortcuts import render,redirect,get_object_or_404
from restuarant.models import place,restuarants,menu


def addpage(request):
    Place = place.objects.all()
    Restuarant = restuarants.objects.all()
    return render(request,'CUD/addoption.html',{'place':Place,'restuarant':Restuarant})

def addplace(request):
    p = place()
    p.PlaceName = request.POST['placename']
    p.save()
    return redirect('cud:Add')

def addrestuarant(request):
    r = restuarants()
    r.PlaceCode = place.objects.get(id=request.POST['place'])
    r.restName = request.POST['restuarantname']
    r.restPic = request.FILES['restuarantpic']
    r.rating = 0.0
    r.save()
    return redirect('cud:Add')

def addmenu(request):
    m = menu()
    m.restcode = restuarants.objects.get(id=request.POST['restuarant'])
    m.menuName = request.POST['menuname']
    m.menupic = request.FILES['menupic']
    m.price = float(request.POST['menuprice'])
    m.rating = 0.0
    m.save()
    return redirect('cud:Add')
