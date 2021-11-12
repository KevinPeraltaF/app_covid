
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
from covid import views as key
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('covid.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = key.Error404View.as_view()
handler500 = key.Error500View.as_error_view()
