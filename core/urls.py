from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('',include('api.urls')),
    path('tags/',include('tags.urls')),
    path('reviews/',include('reviews.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    
]

