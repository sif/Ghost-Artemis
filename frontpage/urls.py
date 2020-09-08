"""Path list for this app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='frontpage'),
    path('contact/', views.contact, name='contact'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
    path('quote/', views.quote, name='quote'),
]
