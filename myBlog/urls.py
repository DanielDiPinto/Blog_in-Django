from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('crm.urls')),
    path('captcha/', include('captcha.urls')),
]
