# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/h/helvruxw/issue.kunsthaus.ru/issue')
sys.path.insert(1, '/home/h/helvruxw/issue.kunsthaus.ru/venv/lib/python2.7')
os.environ['DJANGO_SETTINGS_MODULE'] = 'issue.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# -*- coding: utf-8 -*-
#import os, sys
#sys.path.append('/home/h/helvruxw/kunsthaus.ru/kunsthaus')
#sys.path.append('/home/h/helvruxw/kunsthaus.ru/venv/lib/python2.7')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'kunsthaus.settings'
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
