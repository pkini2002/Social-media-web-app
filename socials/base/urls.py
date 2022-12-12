from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('otherprofile/', views.otherprofile,name='otherprofile'),
    # path('profileUpdate/', views.profileUpdate,name='profileUpdate'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)