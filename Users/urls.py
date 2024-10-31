#url:

from django.urls import path
from Users import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup_page, name="signup"),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.Ulogout, name='logout'),
]
