from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/registration/',
    #     UserCreateView.as_view(),
    #     name='registration'),
    path('auth/',
         include('django.contrib.auth.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
