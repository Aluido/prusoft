from django.urls import path
from django.conf.urls.static import static
from presentacion1 import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('<int:receta_id>/', views.detail, name='detail'),
]
