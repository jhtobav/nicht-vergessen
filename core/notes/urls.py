from django.urls import path

from . import views

urlpatterns = [
    # ex: /notes/
    path('', views.notes, name='notes'),
    # ex: /notes/1
    path('<int:note_id>/', views.note_details, name='note_details'),
]