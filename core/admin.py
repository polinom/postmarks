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
    list_display = ('image', 'name', 'description', 'year')
    inlines = [ PriceAndTimeSoldInline,]
    list_filter = ('year',)
    list_per_page = 20
    
    formfield_overrides = {
                        models.ImageField: {'widget': AdminImageWidget},
                        models.URLField: {'widget': URLFieldWidget}
                       }
                       
# ----------------------  Raritet stamps admin ----------------------------

class PriceAndTimeSoldInline2(admin.TabularInline):
    model = PriceAndTimeSold2
    fields = ['start_price','sold_price','time','auction',]
    extra = 1

class StampModelAdmin2(admin.ModelAdmin):
    list_display = ('image', 'name', 'description', 'year')
    inlines = [ PriceAndTimeSoldInline2,]
    list_filter = ('year',)
    list_per_page = 20

    formfield_overrides = {
                           models.ImageField: {'widget': AdminImageWidget},
                           models.URLField: {'widget': URLFieldWidget}
                          }

# ------------------------- eBay Stamps Admin ------------------------------

class eBayPriceAndTimeSoldInline(admin.TabularInline):
    model = eBayPriceAndTimeSold
    fields = ['start_price','sold_price','time','auction',]
    extra = 1

class eBayStampModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'description', 'year')
    inlines = [ eBayPriceAndTimeSoldInline,]
    list_filter = ('year',)
    list_per_page = 20

    formfield_overrides = {
                           models.ImageField: {'widget': AdminImageWidget},
                           models.URLField: {'widget': URLFieldWidget}
                          }

# ------------------------ Molotok Syamp Admin -------------------------------
class MolotokPriceAndTimeSoldInline(admin.TabularInline):
    model = MolotokPriceAndTimeSold
    fields = ['start_price','sold_price','time','auction',]
    extra = 1

class MolotokStampModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'description', 'year', 'date', 'sold_price', 'start_price')
    inlines = [ MolotokPriceAndTimeSoldInline,]
    list_filter = ('year',)
    list_per_page = 20

    formfield_overrides = {
                           models.ImageField: {'widget': AdminImageWidget},
                           models.URLField: {'widget': URLFieldWidget}
                          }


admin.site.register(eBayStamp,eBayStampModelAdmin)    
admin.site.register(MolotokStamp,MolotokStampModelAdmin)  
admin.site.register(Stamp2,StampModelAdmin2)    
admin.site.register(Stamp,StampModelAdmin)