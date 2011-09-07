from django.core.management.base import BaseCommand
from urllib2 import urlopen
from urllib import urlretrieve
from BeautifulSoup import BeautifulSoup
from core.models import Stamp, PriceAndTimeSold
from django.conf import settings
import datetime


URL = 'http://www.cherrystoneauctions.com/_auction/results1.asp?auction=&country=&sn=7443&group=817&pagenum=1'

class Command(BaseCommand):
    help = """
    Hello
           """
    def handle(self, *args, **options):
        page = BeautifulSoup(urlopen(url))
        