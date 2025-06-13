
from django.contrib import admin
from django.urls import path, include

import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("user_profile.urls")),
]

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)