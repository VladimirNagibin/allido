from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='about'),
    # path('rules/', views.Rules.as_view(), name='rules'),
]
