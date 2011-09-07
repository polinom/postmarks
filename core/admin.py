from django.contrib import admin
from models import Stamp, PriceAndTimeSold, Picture, Stamp2, PriceAndTimeSold2
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
    
    
admin.site.register(Stamp2,StampModelAdmin2)    
admin.site.register(Stamp,StampModelAdmin)