# это URL-декларации текущего проекта Django, или, иначе говоря, это
# «диспетчер URL-aдpecoв» Django-пpoeктa;

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')

application = get_wsgi_application()
