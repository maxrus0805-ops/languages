from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('language/<int:language_id>/', views.language_detail, name='language_detail'),
    path('popular/', views.popular_languages, name='popular_languages'),
]