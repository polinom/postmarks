#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from urllib2 import urlopen
from urllib import urlretrieve
from BeautifulSoup import BeautifulSoup
from core.models import Stamp2, PriceAndTimeSold2
from django.conf import settings
import datetime


settings.MEDIA_ROOT

MAIN_STAMP_PIC = 'main_stamp2_pic/'

RARITET_SITE = 'http://www.raritanstamps.com/Cat/LotsView.php3?LotF=792&LotL=1162'
RARITET_SITE = 'http://www.raritanstamps.com/Cat/LotsView.php3?LotF=206&LotL=239'
RARITET_SITE = 'http://www.raritanstamps.com/Cat/LotsView.php3?LotF=1420&LotL=1877'

ROOT_SITE = 'http://www.raritanstamps.com/Cat/'

class Command(BaseCommand):
    help = """
    Hello
           """
    def handle(self, *args, **options):
        page = urlopen(RARITET_SITE)
        page = BeautifulSoup(page)
        trs = page('tr')
        for tr in trs:
            tds = tr('td')
            if len(tds[4]('a')):
                cat_num = tds[2].getText()
                url_to_page = ROOT_SITE+tds[4]('a')[0].get('href')
                item_page = BeautifulSoup(urlopen(url_to_page))
                    
                    
                image_url = ROOT_SITE+item_page('img')[0].get('src')
                image_name = image_url.split('/')[-1]
                urlretrieve(image_url, settings.MEDIA_ROOT+MAIN_STAMP_PIC+image_name)
                    
                description = tds[3].getText()
                    
                    
                try:
                    year = int(description.strip()[:4])
                except:
                    year = 0
                    
                    
                name = tds[0].getText().strip()
                    
                price = float(tds[5].getText().replace('&nbsp;','').strip())
                    
                print '---------------------'
                print year
                print price
                print name
                print description
                print image_url
                print url_to_page
                name = name + '(51)'
                stamp = Stamp2.objects.create(name=name, description=description, url=url_to_page, year=year, main_picture = MAIN_STAMP_PIC+image_name)
                PriceAndTimeSold2.objects.create(stamp=stamp, start_price = price, auction=3, time=datetime.datetime(2011, 9, 8, 00, 00, 00))
