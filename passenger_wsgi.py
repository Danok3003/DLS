# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2730334/data/www/detectproject.ru/detection_site')
sys.path.insert(1, '/var/www/u2730334/data/detectenv/lib/python3.10.1/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'detection_site.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()