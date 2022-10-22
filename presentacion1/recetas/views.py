from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView
from .models import Receta

# Create your views here.
def index(request):
	recetas_list = Receta.objects.all()
	context = {
		'recetas_list': recetas_list
	}
	return render(request,'recetas/index.html', context)

def detail(request,receta_id):
	receta = get_object_or_404(Receta, pk=receta_id)
	context = {
		'receta': receta,
	}
	return render(request, 'recetas/detail.html', context)
	