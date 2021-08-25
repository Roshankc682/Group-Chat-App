from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    # admin Roshankc@@123
    path('admin/', admin.site.urls),
    path('', views.register),
    path('username', views.save_username),
    path('login/', views.login),
    path('check', views.check_login),
    path('chat_group/', views.home),
    path('logout', views.logout_view),
    path('message', views.message, name='message'),
    path('message_return', views.message_return, name='message'),

    
]
# make debug False
handler404 = views.page_not_found_view

# python manage.py collectstatic
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)