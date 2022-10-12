from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
     path('error/', views.error,name='error'),
    path('logout/', views.logout,name='logout'),
    path('signup/', views.signup,name='signup'),
    path('friends/', views.friends,name='friends'),
    path('profile/', views.profile,name='profile'),
    path('post/', views.post,name='post'),
    path('otherprofile/', views.otherprofile,name='otherprofile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)