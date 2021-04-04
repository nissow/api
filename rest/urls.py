from django.urls import path
from . import views

urlpatterns = [
    path('',views.Med),
    path('Medicament-list/',views.MedList),
    path('Medicament-create/',views.MedCreate),
    path('Medicament-update/<str:pk>',views.MedUpdate)
]
