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
        if self.id:
            price_objs = PriceAndTimeSold.objects.filter(stamp=self).order_by('time')
            self.ptime = [price.time for price in price_objs]
            self.psold_price = [price.sold_price for price in price_objs]
            self.pstart_price = [price.start_price for price in price_objs]

    def date(self):
        strng = ''
        for item in self.ptime:
            strng += '<div>'
            strng += str(item.date())
            strng += '</div><br\>'
        return strng

    def sold_price(self):
        strng = ''
        for item in self.psold_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng

    def start_price(self):
        strng = ''
        for item in self.pstart_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng
    
    
    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url
    
    
    def unicode(self):
        return name
        
    class Meta:
        verbose_name = "cherrystoneauctions stamp"
        verbose_name_plural = "cherrystoneauctions stamps"
    
    image.allow_tags = True
    date.allow_tags = True
    sold_price.allow_tags = True
    start_price.allow_tags = True


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
        if self.id:
            price_objs = PriceAndTimeSold2.objects.filter(stamp=self).order_by('time')
            self.ptime = [price.time for price in price_objs]
            self.psold_price = [price.sold_price for price in price_objs]
            self.pstart_price = [price.start_price for price in price_objs]

    def date(self):
        strng = ''
        for item in self.ptime:
            strng += '<div>'
            strng += str(item.date())
            strng += '</div><br\>'
        return strng

    def sold_price(self):
        strng = ''
        for item in self.psold_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng

    def start_price(self):
        strng = ''
        for item in self.pstart_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng


    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url


    def unicode(self):
        return name
        
        
    class Meta:
        verbose_name = "raritan stamp"
        verbose_name_plural = "raritan stamps"

    image.allow_tags = True
    date.allow_tags = True
    sold_price.allow_tags = True
    start_price.allow_tags = True
    
    
    
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
        if self.id:
            price_objs = eBayPriceAndTimeSold.objects.filter(stamp=self).order_by('time')
            self.ptime = [price.time for price in price_objs]
            self.psold_price = [price.sold_price for price in price_objs]
            self.pstart_price = [price.start_price for price in price_objs]

    def date(self):
        strng = ''
        for item in self.ptime:
            strng += '<div>'
            strng += str(item.date())
            strng += '</div><br\>'
        return strng

    def sold_price(self):
        strng = ''
        for item in self.psold_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng

    def start_price(self):
        strng = ''
        for item in self.pstart_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng


    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url


    def unicode(self):
        return name

    image.allow_tags = True
    date.allow_tags = True
    sold_price.allow_tags = True
    start_price.allow_tags = True
    
    
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
        if self.id:
            price_objs = MolotokPriceAndTimeSold.objects.filter(stamp=self).order_by('time')
            self.ptime = [price.time for price in price_objs]
            self.psold_price = [price.sold_price for price in price_objs]
            self.pstart_price = [price.start_price for price in price_objs]

    def date(self):
        strng = ''
        for item in self.ptime:
            strng += '<div>'
            strng += str(item.date())
            strng += '</div><br\>'
        return strng

    def sold_price(self):
        strng = ''
        for item in self.psold_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng

    def start_price(self):
        strng = ''
        for item in self.pstart_price:
            strng += '<div>'
            strng += str(item)
            strng += '</div><br\>'
        return strng

    def unicode(self):
        return name

    def image(self):
        return '<img width="100" src="%s">'%self.main_picture.url


    image.allow_tags = True
    date.allow_tags = True
    sold_price.allow_tags = True
    start_price.allow_tags = True
    
    
class MolotokPriceAndTimeSold(models.Model):
    stamp = models.ForeignKey(MolotokStamp)
    time = models.DateTimeField(null=True, blank=True)
    start_price = models.FloatField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    auction = models.PositiveIntegerField(choices=AUCTION_SITES)

# ---------------------------------------------------------------------------------------











