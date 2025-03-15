from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/cse/', views.cse, name='cse'),  # Ensure this exists
    path('departments/ece/', views.ece, name='ece'),
    path('departments/mech/', views.mech, name='mech'),
    path('departments/civil/', views.civil, name='civil'),
    path('contact/', views.contact, name='contact'),
]
