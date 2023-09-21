# точка входа для АSGI-совместимых веб-серверов, обслуживающих ваш
# проект (он потребуется при развертывании приложения на публичном сайте);

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')

application = get_asgi_application()
