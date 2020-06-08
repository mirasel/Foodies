from django.db import models
from django.conf import settings
from django.db import models

class place(models.Model):
    PlaceName= models.CharField(max_length=40)

    def __str__(self):
        return self.PlaceName

class restuarants(models.Model):
    PlaceCode= models.ForeignKey('place',models.CASCADE)
    restPic = models.ImageField(upload_to='images/')
    restName= models.CharField(max_length=50)
    rating = models.FloatField(max_length=10)

    def __str__(self):
        return self.restName

class menu(models.Model):
    restcode = models.ForeignKey('restuarants',models.CASCADE)
    menupic = models.ImageField(upload_to='images/')
    menuName = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    rating = models.FloatField(max_length=50)

    def __str__(self):
        return self.menuName +' - '+str(self.price)

class usermenurating(models.Model):
    ratingcode = models.ForeignKey('menu',models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,)
    rating = models.FloatField(max_length=10)

    def __str__(self):
        return str(self.user)+'-'+str(self.ratingcode)+'-'+str(self.rating)
