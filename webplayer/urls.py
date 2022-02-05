from django.urls import path,include,re_path
from . import views
from django.contrib.staticfiles.views import serve
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.login,name='loginpage'),
    path('qa/',views.assessment,name='assessment'),
    path('thanks/',views.thanksPage,name='thankspage'),
    path('favicon.ico', serve, {'path': 'img/favicon.ico'}),
    re_path(r'^get_quality/$',views.get_quality),
    re_path(r'^get_next/$',views.get_next_video)
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
