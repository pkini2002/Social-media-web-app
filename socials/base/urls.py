from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
     path('friends/', views.friends,name='friends'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)