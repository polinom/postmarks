from django.db import models

# Create your models here.


class Stamp(models.Model):
    main_picture = models.ImageField(upload_to = 'main_stamp_pic')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True ,editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    
    
    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url
    
    
    def unicode(self):
        return name
    
    image.allow_tags = True

AUCTION_SITES = [
              (0,'eBuy.com'),
              (1,'Molotok.ru'),
              (2,'dasdsadsa'),
              (3,'bfdfdgfd'),
                ]

    
class PriceAndTimeSold(models.Model):
    stamp = models.ForeignKey(Stamp)
    time = models.DateTimeField()
    price = models.FloatField()
    auction = models.PositiveIntegerField(choices=AUCTION_SITES)
    

class Picture(models.Model):
    picture = models.ImageField(upload_to = 'other_stamp_pic')
    stamp = models.ForeignKey(Stamp)