from django.urls import path

from . import views

app_name = 'ratings'
urlpatterns = [
    path('', views.ratings, name='ratings'),
    path('<int:rating_id>/', views.rating_details, name='rating_details'),
    path('create/', views.rating_create, name='rating_create'),
]