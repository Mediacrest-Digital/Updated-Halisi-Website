from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Halisi Family Hospital"
admin.site.site_title = "Halisi Family Hospital"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.website.urls", namespace="website")),
]

urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



