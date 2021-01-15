from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    # home
    path('', views.index, name='home'),
    
    # Registration
    path('registration/', views.registration_view, name='register'),
    
    # Login
    path('login/', views.login_view, name='login'),
    
    # Logout
    path('logout/', views.logout_view, name='logout'),
]
