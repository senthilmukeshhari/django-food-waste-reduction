from django.urls import path
from food_listing import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('nearest-foods', views.nearest_foods, name='nearest_foods'),
]
