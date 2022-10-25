from django.test import TestCase, Client
from recetas.models import Receta

# Create your tests here.
# The tests are run with >./manage.py test --keepdb

class RecetasTestCase(TestCase):
	# Cliente para ejecutar consultas a la pagina
	client = Client()
	
	# Carga de datos previo a la prueba en caso de ser necesario
	def setUp(self):
		return
	
	# Prueba de creacion de Recetas
	def test_create(self):
		with open('testImage.jpeg', 'rb') as testImage:
			response = self.client.post('/recetas/create/', {
				'titulo': ['TituloPrueba'],
				'detalle': ['DetallePrueba'],
				'ingredientes': ['IngredientesPrueba'],
				'imagen': testImage
			})
			print(response.status_code)
			# TODO: arreglar

	# Prueba de visualización de Recetas
	def test_index(self):
		response = self.client.get('/recetas/')
		print(response.content)
