from django.db import models

# Create your models here.


class Stamp(models.Model):
    main_picture = models.ImageField(upload_to = 'main_stamp_pic')
    name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True ,editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    url = models.URLField(max_length=150, verify_exists=False, null=True, blank=True)
    
    
    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url
    
    
    def unicode(self):
        return name
    
    image.allow_tags = True


AUCTION_SITES = [
              (0,'eBuy.com'),
              (1,'Molotok.ru'),
              (2,'www.cherrystoneauctions.com'),
              (3,'www.raritanstamps.com'),
              (4,'-- not implemented --'),
                ]

class PriceAndTimeSold(models.Model):
    stamp = models.ForeignKey(Stamp)
    time = models.DateTimeField(null=True, blank=True)
    start_price = models.FloatField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    auction = models.PositiveIntegerField(choices=AUCTION_SITES)

class Picture(models.Model):
    picture = models.ImageField(upload_to = 'other_stamp_pic')
    stamp = models.ForeignKey(Stamp)
