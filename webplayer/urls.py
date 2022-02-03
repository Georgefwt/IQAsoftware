from django.urls import path,include,re_path
from . import views
from django.contrib.staticfiles.views import serve
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.assessment,name='assessment'),
    path('favicon.ico', serve, {'path': 'img/favicon.ico'}),
    re_path(r'^get_quality/$',views.get_quality)
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
