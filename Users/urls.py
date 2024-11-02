#url:

from django.urls import path
from Users import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup_page, name="signup"),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.Ulogout, name='logout'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
