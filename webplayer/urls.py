from django.urls import path,include
from . import views
from django.contrib.staticfiles.views import serve
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.assessment,name='assessment'),
    path('favicon.ico', serve, {'path': 'img/favicon.ico'}),
    # path('article<int:id>/', views.article_detail, name='article_detail'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
