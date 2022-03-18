from django.urls import path,include,re_path
from . import views
from django.contrib.staticfiles.views import serve
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.login,name='loginpage'),
    path('login_check/',views.login_check,name='logincheckpage'),
    path('login_fail/',views.login_fail,name="loginfailpage"),
    path('preqa/',views.preassessment,name='preassessment'),
    path('qa/',views.assessment,name='assessment'),
    path('thanks/',views.thanksPage,name='thankspage'),
    path('notice/',views.notice,name='notice'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('get_quality/',views.get_quality),
    path('get_next/',views.get_next_video),
    path('available/',views.available,name='availableserialpage')
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
