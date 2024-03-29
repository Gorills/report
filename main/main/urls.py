from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
   
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('metrika/', include('metrika.urls')),
    path('seo/', include('seobrain.urls')),
    path('', include('home.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "home.views.page_not_found_view"
