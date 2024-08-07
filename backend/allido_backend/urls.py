from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from users.views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/registration/',
         UserCreateView.as_view(),
         name='registration'),
    path('auth/',
         include('django.contrib.auth.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
