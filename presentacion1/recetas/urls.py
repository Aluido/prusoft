from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('<int:receta_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('lci/', views.get_last_id, name='lci'),
]
