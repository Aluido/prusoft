from django.test import TestCase, Client
from  django.middleware.csrf import get_token
from recetas.models import Receta
import hashlib

# Create your tests here.
# The tests are run with >./manage.py test --keepdb

class RecetasTestCase(TestCase):
	# Cliente para ejecutar consultas a la pagina
	client = Client()
	
	# Carga de datos previo a la prueba en caso de ser necesario
	def setUp(self):
		print("===DATOS PRE-INGRESADOS PARA LA PRUEBA===")
		with open('testImage.jpeg', 'rb') as testImage:
			self.client.post('/recetas/create/', {
				'titulo': ['Pie con Queso'],
				'detalle': ['- Haz un pie\n- Ponle Queso\n- A comer!'],
				'ingredientes': ['- Pie\n- Queso'],
				'imagen': testImage
			})
		print('- Pie con Queso')
	
	# Prueba de creacion de Recetas
	def test_create(self):
		print('===INICIO PRUEBA DE CREACIÓN DE RECETAS===')
		with open('testImage.jpeg', 'rb') as testImage:
			print('Nueva receta añadida por POST: Bistec a lo prueba....')
			response = self.client.post('/recetas/create/', {
				'titulo': ['Bistec a lo prueba'],
				'detalle': ['- Tome un bistec\n- Paselo por unit testing\n- A comer!'],
				'ingredientes': ['- Bistec\n- Unit testing'],
				'imagen': testImage
			})
		if (response.status_code != 302):
			print('Error al añadir la receta de prueba.')
			print('===FIN PRUEBA DE CREACIÓN DE RECETAS===\n')
			return False
		else:
			print('Ejecución consulta GET de las Recetas almacenadas....')
			ret_val = True
			response = self.client.get('/recetas/')
			print('Respuesta del servidor:')
			print('HTTP status_code:', response.status_code)
			if response.status_code != 200:
				print('No se recibió una respuesta HTTP 200')
				ret_val = False
			print('HTML:', response.content)
			html_hash = hashlib.md5(response.content).hexdigest()
			print('MD5 Hash:', html_hash)
			if html_hash != 'b7342e1042745217b030679bc3e9ef88':
				print('El hash MD5 del archivo HTML no es el esperado.')
				ret_val = False               
			print('===FIN PRUEBA DE CREACIÓN DE RECETAS===\n')
			return ret_val

	# Prueba de visualización de Recetas
	def test_index(self):
		print('===INICIO PRUEBA DE VISUALIZACIÓN DE RECETAS===')
		response = self.client.get('/recetas/1/')
		print('Respuesta del servidor:')
		print('HTTP status_code:', response.status_code)
		print('HTML:', response.content)
		print('===FIN PRUEBA DE VISUALIZACIÓN DE RECETAS===\n')
		if(response.status_code != 200):
			return False
		else:
			return True
	
	# Prueba de edición de Recetas
	def test_edit(self):
		print('===INICIO PRUEBA DE EDICIÓN DE RECETAS===')
		with open('testImage.jpeg', 'rb') as testImage:
			print('Receta modificada por POST: Pie con Queso....')
			response = self.client.post('/recetas/edit/1', {
				'titulo': ['Pie con Ultra Queso'],
				'detalle': ['- Haz un super pie\n- Ponle aún más queso\n- A recontra comer!'],
				'ingredientes': ['- Poderoso Pie\n- Ultra Queso'],
				'imagen': testImage
			})
		if (response.status_code != 302):
			print('Error al editar la receta.')
			return False
		else:
			print('Ejecución consulta GET de la Receta modificada....')
			response = self.client.get('/recetas/1/')
			print('Respuesta del servidor:')
			print('HTTP status_code:', response.status_code)
			print('HTML:', response.content)
		print('===FIN PRUEBA DE EDICIÓN DE RECETAS===\n')
		return True
	
	# Prueba de eliminación de Recetas
	def test_delete(self): # Alberto: No comprendo si "borrar info" se refiere a eliminar una receta o sus detalles
		print('===INICIO PRUEBA DE ELIMINACIÓN DE RECETAS===')
		print('Ejecución consulta POST para eliminar: Pie con Queso....')
		with open('testImage.jpeg', 'rb') as testImage:
			print('Receta eliminada por POST: Pie con Queso....')
			response = self.client.post('/recetas/delete/1', {
				'titulo': ['Pie con Queso'],
				'detalle': ['- Haz un pie\n- Ponle Queso\n- A comer!'],
				'ingredientes': ['- Pie\n- Queso'],
				'imagen': testImage
			})
		response = self.client.get('/recetas/')
		if(response.status_code != 200):
			print('Error al eliminar.')
			print('===FIN PRUEBA DE ELIMINACIÓN DE RECETAS===\n')
			return False
		else:
			print('Respuesta del servidor:')
			print('HTTP status_code:', response.status_code)
			print('HTML:', response.content)
			print('===FIN PRUEBA DE ELIMINACIÓN DE RECETAS===\n')
			return True
