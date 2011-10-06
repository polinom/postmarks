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


    def __init__(self, *args, **kwargs):
        super(Stamp, self).__init__(*args, **kwargs)
        price_obj = PriceAndTimeSold.objects.filter(stamp=self).order_by('time')[0]
        self.ptime = price_obj.time
        self.psold_price = price_obj.sold_price
        self.pstart_price = price_obj.start_price

    def date(self):
        return str(self.ptime.date())

    def sold_price(self):
        return self.psold_price

    def start_price(self):
        return self.pstart_price
    
    
    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url
    
    
    def unicode(self):
        return name
        
    class Meta:
        verbose_name = "cherrystoneauctions stamp"
        verbose_name_plural = "cherrystoneauctions stamps"
    
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
    
# -------------------------  ------------------------------------------------------------------
class Stamp2(models.Model):
    main_picture = models.ImageField(upload_to = 'main_stamp2_pic')
    name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True ,editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    url = models.URLField(max_length=150, verify_exists=False, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super(Stamp2, self).__init__(*args, **kwargs)
        price_obj = PriceAndTimeSold2.objects.filter(stamp=self).order_by('time')[0]
        self.ptime = price_obj.time
        self.psold_price = price_obj.sold_price
        self.pstart_price = price_obj.start_price

    def date(self):
        return str(self.ptime.date())

    def sold_price(self):
        return self.psold_price

    def start_price(self):
        return self.pstart_price


    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url


    def unicode(self):
        return name
        
        
    class Meta:
        verbose_name = "raritan stamp"
        verbose_name_plural = "raritan stamps"

    image.allow_tags = True
    
    
    
class PriceAndTimeSold2(models.Model):
    stamp = models.ForeignKey(Stamp2)
    time = models.DateTimeField(null=True, blank=True)
    start_price = models.FloatField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    auction = models.PositiveIntegerField(choices=AUCTION_SITES)

# ------------------------ EBAY ---------------------------------------------------------

class eBayStamp(models.Model):
    main_picture = models.ImageField(upload_to = 'ebay_stamp_pic')
    name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True ,editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    url = models.URLField(max_length=150, verify_exists=False, null=True, blank=True)



    def __init__(self, *args, **kwargs):
        super(eBayStamp, self).__init__(*args, **kwargs)
        price_obj = eBayPriceAndTimeSold.objects.filter(stamp=self).order_by('time')[0]
        self.ptime = price_obj.time
        self.psold_price = price_obj.sold_price
        self.pstart_price = price_obj.start_price

    def date(self):
        return str(self.ptime.date())

    def sold_price(self):
        return self.psold_price

    def start_price(self):
        return self.pstart_price


    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url


    def unicode(self):
        return name

    image.allow_tags = True
    
    
class eBayPriceAndTimeSold(models.Model):
    stamp = models.ForeignKey(eBayStamp)
    time = models.DateTimeField(null=True, blank=True)
    start_price = models.FloatField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    auction = models.PositiveIntegerField(choices=AUCTION_SITES)

# ---------------------------------------------------------------------------------------



# ------------------------ EBAY ---------------------------------------------------------

class MolotokStamp(models.Model):
    main_picture = models.ImageField(upload_to = 'molotok_stamp_pic')
    name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True ,editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    url = models.URLField(max_length=150, verify_exists=False, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super(MolotokStamp, self).__init__(*args, **kwargs)
        price_obj = MolotokPriceAndTimeSold.objects.filter(stamp=self).order_by('time')[0]
        self.ptime = price_obj.time
        self.psold_price = price_obj.sold_price
        self.pstart_price = price_obj.start_price

    def date(self):
        return str(self.ptime.date())

    def sold_price(self):
        return self.psold_price

    def start_price(self):
        return self.pstart_price


    def unicode(self):
        return name

    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url


    image.allow_tags = True
    
    
class MolotokPriceAndTimeSold(models.Model):
    stamp = models.ForeignKey(MolotokStamp)
    time = models.DateTimeField(null=True, blank=True)
    start_price = models.FloatField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    auction = models.PositiveIntegerField(choices=AUCTION_SITES)

# ---------------------------------------------------------------------------------------











