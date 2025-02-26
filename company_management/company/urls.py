from django.urls import path
from .views import company_list, add_company, edit_company, delete_company

urlpatterns = [
    path('', company_list, name='company_list'),
    path('add/', add_company, name='add_company'),
    path('edit/<str:company_id>/', edit_company, name='edit_company'),
    path('delete/<str:company_id>/', delete_company, name='delete_company'),
]
