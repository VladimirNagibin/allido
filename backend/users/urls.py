from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('', views.BirthdayCreateView.as_view(), name='create'),
    # path('list/', views.BirthdayListView.as_view(), name='list'),
    path('profile/<slug:username>/',
         views.UserDetailView.as_view(),
         name='profile'),
    path(
        'edit_profile/',
        views.ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
    # path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    # path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
]
