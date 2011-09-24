#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from urllib2 import urlopen
from urllib import urlretrieve
from BeautifulSoup import BeautifulSoup
from core.models import MolotokStamp, MolotokPriceAndTimeSold
from django.conf import settings
import datetime
import re


settings.MEDIA_ROOT

MAIN_STAMP_PIC = 'molotok_stamp_pic/'

MOLOTOK_SITE = 'http://molotok.ru/listing.php/search?buy=2&category=48370&description=1&p={page}&string=%D1%80%D0%B0%D0%B7%D0%BD&change_view=1'
ROOT_SITE = 'http://molotok.ru'

class Command(BaseCommand):
    help = """
    Hello
           """
    def handle(self, *args, **options):
        page = 1
        while page:
            p = urlopen(MOLOTOK_SITE.format(page=page))
            p = BeautifulSoup(p)
            trs = p('tr')
            if len(trs):
                for tr in trs[3:]:

                    a = tr('a', {'class':'popupTrigger'})[0]
                    name = a.get('title')
                    page_url = ROOT_SITE+a.get('href')
                    image_url = a.get('data-img').replace('64x48','oryginal')
                    image_name = image_url.split('/')[-1]+'.jpg'
                    tds = tr('td')
                    price_us = float(tds[2]('span',{'class':'small'})[0].text.replace('(&#8776;','').replace(' $)','').replace(',','.').replace(' ',''))
                    to_end = tds[5].text
                    hours, days = 0, 0
                    if u'час' in to_end:
                        hours = int(to_end.replace(u' час.',u''))
                    elif u'дн' in tds[5].text:
                        days = int(to_end.replace(u' дн.',u''))

                    auc_date = datetime.datetime.now()+datetime.timedelta(hours=hours, days=days)
                    print auc_date
                    years = re.findall(r'19\d\d', name)
                    year = 0
                    if len(years):
                        year = years[0] 
                    
                    stamp,created = MolotokStamp.objects.get_or_create(url=page_url, defaults = {'name':name, 'description':name, 'year':year, 'main_picture' : MAIN_STAMP_PIC+image_name})
                    if created:
                        urlretrieve(image_url, settings.MEDIA_ROOT+MAIN_STAMP_PIC+image_name)
                        MolotokPriceAndTimeSold.objects.create(stamp=stamp, start_price = price_us, auction=1, time=auc_date)

                page += 1
            else:
                page = 0