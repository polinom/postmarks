from django.core.management.base import BaseCommand
from urllib2 import urlopen
from urllib import urlretrieve
from BeautifulSoup import BeautifulSoup
from core.models import Stamp, PriceAndTimeSold
from django.conf import settings
import datetime


URL = 'http://dl.dropbox.com/u/15842180/x.html'

class Command(BaseCommand):
    help = """
    Hello
           """
    def handle(self, *args, **options):
        p = BeautifulSoup(urlopen(URL))
        trs = p('tr',{'bgcolor':'#EEEEEE'})+p('tr',{'bgcolor':'#DDDDDD'})
        for tr in trs:
            tds = tr('td')
            number = tds[1].getText()
            if len(tds) == 13:
                price = tds[11].getText().replace('$','').replace('BIDDING CLOSED','').replace(',','')
                stamp = Stamp.objects.filter(name=number.strip())
                if stamp.count():
                    price_obj = stamp[0].priceandtimesold_set.all()[0]
                    price_obj.sold_price = float(price)
                    price_obj.save()
                    print stamp[0].name