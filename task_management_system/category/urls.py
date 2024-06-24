from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_category, name='add_category'),
    # path('edit/<int:id>', views.edit_category, name='edit_category'),
]