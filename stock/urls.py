from django.urls import path, include

from stock import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.get_symbol_data, name='get_symbol_data'),
    path('download_data', views.download_data, name='download_data')
]