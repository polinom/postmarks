from django.contrib import admin
from models import Stamp, PriceAndTimeSold, Picture




class PriceAndTimeSoldInline(admin.TabularInline):
    model = PriceAndTimeSold
    fields = ['price','time','auction',]

class StampModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', )
    inlines = [ PriceAndTimeSoldInline,]
    
    
    
admin.site.register(Stamp,StampModelAdmin)