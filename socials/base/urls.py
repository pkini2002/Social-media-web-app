from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PasswordsChangeView,ShowProfilePageView,EditProfilePageView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
     path('error/', views.error,name='error'),
    path('logout/', views.logout,name='logout'),
    path('signup/', views.signup,name='signup'),
    path('friends/', views.friends,name='friends'),
    path('profile/', views.profile,name='profile'),
    path('post/', views.post,name='post'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    # path('otherprofile/', views.otherprofile,name='otherprofile'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name='show_profile_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)