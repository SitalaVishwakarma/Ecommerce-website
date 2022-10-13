from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "ShopNow Admin"
admin.site.site_title = "ShopNow Admin Portal"
admin.site.index_title = "Welcome to ShopNow"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]
