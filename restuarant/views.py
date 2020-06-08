from django.shortcuts import render,redirect,get_object_or_404
from .models import restuarants,menu,usermenurating
from django.contrib.auth.models import User
from django.db.models import Avg
from django.urls import reverse

def homepage(request):
    rest = restuarants.objects.all()
    return render(request,'restuarant/home.html',{'rest':rest})

def _menu(request,r_id):
    restuarant = restuarants.objects.all()
    rt = get_object_or_404(restuarants,pk=r_id)
    return render(request,'restuarant/menu.html',{'rest':rt,'restid':r_id,'restuarant':restuarant,'restname':rt.restName})

def rateit(request):
    if request.method == 'POST':
        try:
            userrating = usermenurating.objects.get(user=User.objects.get(id=request.POST['userid']),ratingcode=menu.objects.get(id=request.POST['menuid']))
            userrating.rating=request.POST['stars']
            userrating.save()
        except usermenurating.DoesNotExist:
            userrating = usermenurating.objects.create(user=User.objects.get(id=request.POST['userid']),ratingcode=menu.objects.get(id=request.POST['menuid']),rating=request.POST['stars'])
            userrating.save()
        menuratingavg = usermenurating.objects.filter(ratingcode__id=request.POST['menuid']).aggregate(Avg('rating'))
        changemenurate = menu.objects.get(id=request.POST['menuid'])
        changemenurate.rating=menuratingavg['rating__avg']
        changemenurate.save()
        restratingavg = menu.objects.filter(restcode__id=request.POST['r_id']).aggregate(Avg('rating'))
        changerestrate = restuarants.objects.get(id=request.POST['r_id'])
        changerestrate.rating=restratingavg['rating__avg']
        changerestrate.save()
        return redirect(reverse('restuarant:Menu', args={request.POST['r_id']}))

def delete(request,rid,menuid):
    menudelete = menu.objects.filter(id=menuid)
    menudelete.delete()
    row = usermenurating.objects.filter(ratingcode__id=menuid)
    for r in row:
        r.delete()
    return redirect(reverse('restuarant:Menu', args={rid}))

def edit(request):
    m = menu.objects.get(id=request.POST['menuid'])
    m.restcode = restuarants.objects.get(id=request.POST['restuarant'])
    m.menuName = request.POST['menuname']
    if request.POST['pic']:
        m.menupic = request.FILES['menuPic']
    m.price = float(request.POST['menuprice'])
    m.save()
    return redirect(reverse('restuarant:Menu', args={request.POST['r_id']}))
