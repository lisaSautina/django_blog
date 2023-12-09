
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('modules.blog.urls')),
    path('', include('modules.system.urls')),
]
if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #Для работы media в режиме DEBUG = True нам необходимо добавить следующее в backend/urls.py