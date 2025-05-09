from django.urls import path
from mpd_app import views

app_name = "home"
urlpatterns = [
    path('', views.offerta_view, name='offerta'),
    path('privacy/', views.privacy_policy, name='privacy')
]