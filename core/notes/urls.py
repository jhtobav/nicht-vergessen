from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    # ex: /notes/
    path('', views.notes, name='notes'),
    # ex: /notes/1/
    path('<int:note_id>/', views.note_details, name='note_details'),
    # ex: /notes/create/
    path('create/', views.note_create, name='note_create'),
]