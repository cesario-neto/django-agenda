from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),

    # CRUD
    path('contact/create', views.create, name='create'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
]
