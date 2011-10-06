from django.contrib import admin
from models import Stamp, PriceAndTimeSold, Picture, Stamp2, PriceAndTimeSold2,\
                eBayStamp, eBayPriceAndTimeSold, MolotokStamp, MolotokPriceAndTimeSold
from stamps.utils.widgets import AdminImageWidget, URLFieldWidget
from django.db import models


class PriceAndTimeSoldInline(admin.TabularInline):
    model = PriceAndTimeSold
    fields = ['start_price','sold_price','time','auction',]
    extra = 1

class StampModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'description', 'year', 'date', 'sold_price', 'start_price')
    inlines = [ PriceAndTimeSoldInline,]
    list_filter = ('year',)
    list_per_page = 20
    
    formfield_overrides = {
                        models.ImageField: {'widget': AdminImageWidget},
                        models.URLField: {'widget': URLFieldWidget}
                       }
                       
# ----------------------  Raritet stamps admin ----------------------------

class PriceAndTimeSoldInline2(PriceAndTimeSoldInline):
    model = PriceAndTimeSold2

class StampModelAdmin2(StampModelAdmin):
    inlines = [ PriceAndTimeSoldInline2,]


# ------------------------- eBay Stamps Admin ------------------------------

class eBayPriceAndTimeSoldInline(PriceAndTimeSoldInline):
    model = eBayPriceAndTimeSold

class eBayStampModelAdmin(StampModelAdmin):
    inlines = [ eBayPriceAndTimeSoldInline,]

# ------------------------ Molotok Syamp Admin -------------------------------
class MolotokPriceAndTimeSoldInline(PriceAndTimeSoldInline):
    model = MolotokPriceAndTimeSold


class MolotokStampModelAdmin(StampModelAdmin):
    inlines = [ MolotokPriceAndTimeSoldInline,]


admin.site.register(eBayStamp,eBayStampModelAdmin)    
admin.site.register(MolotokStamp,MolotokStampModelAdmin)  
admin.site.register(Stamp2,StampModelAdmin2)    
admin.site.register(Stamp,StampModelAdmin)