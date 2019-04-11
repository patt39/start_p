from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='darry-home'),
    path('about/', views.about, name='darry-about'),
    path('contact/', views.contact, name='darry-contact'),
    path('pricing/', views.pricing, name='darry-pricing'),
    path('work/', views.work, name='darry-workbench'),
]