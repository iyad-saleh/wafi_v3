from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from users import views as user_views

from django.views.generic import TemplateView

urlpatterns =[
    path('staff/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # path("set_language/<str:user_language>/", set_language_from_url, name="set_language_from_url"),

    # path('', include('blog.urls'),name='blog'),
    path('users/', include('users.urls')),
    path('', include('dashboard.urls'), name='dashboard'),





    # path('guest/', include('guest.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
   ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
