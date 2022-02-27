from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.add_image,name = 'home'),
    path('login/',views.user_login,name = 'login'),
    path('celebration/',views.home,name = 'celebration'),
    #path('logout/',views.user_logout,name = 'logout' ),
    path('private/',views.private_image,name = 'private'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)