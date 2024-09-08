from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language

urlpatterns = [
    # URL для смены языка
    path('i18n/setlang/', set_language, name='set_language'),
]

# Локализованные URL
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
)

# Статические и медиа-файлы
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
