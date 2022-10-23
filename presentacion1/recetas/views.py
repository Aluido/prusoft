from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView
from .models import Receta
from .forms import RecetaForm, RecetaDeleteForm
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
	
def create(request):
	if request.method == 'POST':
		form = RecetaForm(request.POST,request.FILES)
		print(form)
		if form.is_valid():
			print('TEEE')
			form.imagen = request.FILES['imagen']
			form.save()
			return redirect('create')
	else:
		form = RecetaForm()
	return render(request, 'recetas/create.html',{'form': form})

def edit(request, pk=None):
	receta = get_object_or_404(Receta, pk=pk)
	if request.method == 'POST':
		form = RecetaForm(request.POST,request.FILES, instance= receta)
		if form.is_valid() and request.FILES:
			form.imagen = request.FILES['imagen']
			form.save()
			return redirect('index')
		elif form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = RecetaForm(instance=receta)
	return render(request, 'recetas/edit.html',{'form': form, 'receta': receta})

def delete(request, pk=None):
	receta = get_object_or_404(Receta, pk=pk)
	if request.method == 'POST':
		form = RecetaDeleteForm(request.POST,request.FILES, instance= receta)
		if form.is_valid():
			receta.delete()
			return redirect('index')
	else:
		form = RecetaDeleteForm(instance=receta)
	return render(request, 'recetas/delete.html',{'form': form, 'receta': receta})