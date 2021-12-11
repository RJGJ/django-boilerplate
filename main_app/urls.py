from django.urls import path

from main_app.views import index, profile

urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/', profile, name="profile")
]
