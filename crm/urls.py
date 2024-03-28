from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register' ),
    path('my-login', views.my_login, name='my-login' ),
    path('dashboard', views.dashboard, name='dashboard' ),
    path('logout', views.user_logout, name='logout' ),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'), 

]
