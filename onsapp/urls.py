from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_asset, name='add_asset'),
    path('update_prices/', views.update_prices, name='update_prices'),
    path('run_ons/', views.execute_ons, name='run_ons'),
    path('delete/<int:asset_id>/', views.delete_asset, name='delete_asset'),
    path('clear_recommendations/', views.clear_recommendations, name='clear_recommendations'),
]