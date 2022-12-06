from django.test import TestCase, Client
from  django.middleware.csrf import get_token
from recetas.models import Receta
from json import loads
import hashlib
import re

# Create your tests here.
# The tests are run with >./manage.py test --keepdb

class RecetasTestCase(TestCase):
	# Cliente para ejecutar consultas a la pagina
	client = Client()
	
	# Carga de datos previo a la prueba en caso de ser necesario
	def setUp(self):
		print("===DATOS PRE-INGRESADOS PARA LA PRUEBA===")
		with open('testImage.jpeg', 'rb') as testImage:
			self.client.post('/create/', {
				'titulo': ['Pie con Queso'],
				'detalle': ['- Haz un pie\n- Ponle Queso\n- A comer!'],
				'ingredientes': ['- Pie\n- Queso'],
				'imagen': testImage
			})
		print('- Pie con Queso')
	
	# Prueba de creacion de Recetas
	def Test_create(self):
		print('===INICIO PRUEBA DE CREACIÓN DE RECETAS===')
		with open('testImage.jpeg', 'rb') as testImage:
			print('Nueva receta añadida por POST: Bistec a lo prueba....')
			response = self.client.post('/create/', {
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
			response = self.client.get('/')
			print('Respuesta del servidor:')
			print('HTTP status_code:', response.status_code)
			if response.status_code != 200:
				print('No se recibió una respuesta HTTP 200')
				ret_val = False
                
			re_html = re.sub(r'testImage_.*\.jpeg', 'testImage.jpeg', response.content.decode())
			print('HTML:', re_html)
			html_hash = hashlib.md5(str.encode(re_html)).hexdigest()
			print('MD5 Hash:', html_hash)
			if html_hash != '1d00d86c268621be079dc9391c78c039':
				print('El hash MD5 del archivo HTML no es el esperado. Recibido:', html_hash)
				ret_val = False               
			print('===FIN PRUEBA DE CREACIÓN DE RECETAS===\n')
			return ret_val

	# Prueba de visualización de Recetas
	def Test_index(self):
		print('===INICIO PRUEBA DE VISUALIZACIÓN DE RECETAS===')
		response = self.client.get(f'/1/')
		print('Respuesta del servidor:')
		print('HTTP status_code:', response.status_code)
		ret_val = True
		re_html = re.sub(r'testImage_.*\.jpeg', 'testImage.jpeg', response.content.decode())
		print('HTML:', re_html)
		html_hash = hashlib.md5(str.encode(re_html)).hexdigest()
		if html_hash != '576649721accc00feb1e750d27557797':
			print('El hash MD5 del archivo HTML no es el esperado. Recibido:', html_hash)
			ret_val = False
		print('===FIN PRUEBA DE VISUALIZACIÓN DE RECETAS===\n')
		if(response.status_code != 200):
			return False
		else:
			return ret_val
	
	# Prueba de edición de Recetas
	def Test_edit(self):
		print('===INICIO PRUEBA DE EDICIÓN DE RECETAS===')
		with open('testImage.jpeg', 'rb') as testImage:
			print('Receta modificada por POST: Pie con Queso....')
			response = self.client.post(f'/edit/1', {
				'titulo': ['Pie con Ultra Queso'],
				'detalle': ['- Haz un super pie\n- Ponle aún más queso\n- A recontra comer!'],
				'ingredientes': ['- Poderoso Pie\n- Ultra Queso'],
				'imagen': testImage
			})
		ret_val = True
		if (response.status_code != 302):
			print('Error al editar la receta.')
			return False
		else:
			print('Ejecución consulta GET de la Receta modificada....')
			response = self.client.get('/1/')
			print('Respuesta del servidor:')
			print('HTTP status_code:', response.status_code)
			re_html = re.sub(r'testImage_.*\.jpeg', 'testImage.jpeg', response.content.decode())
			print('HTML:', re_html)
			html_hash = hashlib.md5(str.encode(re_html)).hexdigest()
			if html_hash != '576649721accc00feb1e750d27557797':
				print('El hash MD5 del archivo HTML no es el esperado. Recibido:', html_hash)
				ret_val = False
		print('===FIN PRUEBA DE EDICIÓN DE RECETAS===\n')
		return ret_val
	
	# Prueba de eliminación de Recetas
	def Test_delete(self): # Alberto: No comprendo si "borrar info" se refiere a eliminar una receta o sus detalles
		print('===INICIO PRUEBA DE ELIMINACIÓN DE RECETAS===')
		print('Ejecución consulta POST para eliminar: Pie con Queso....')
		with open('testImage.jpeg', 'rb') as testImage:
			print('Receta eliminada por POST: Pie con Queso....')
			response = self.client.post(f'/delete/1', {
				'titulo': ['Pie con Queso'],
				'detalle': ['- Haz un pie\n- Ponle Queso\n- A comer!'],
				'ingredientes': ['- Pie\n- Queso'],
				'imagen': testImage
			})
		response = self.client.get('/')
		if(response.status_code != 200):
			print('Error al eliminar.')
			print('===FIN PRUEBA DE ELIMINACIÓN DE RECETAS===\n')
			return False
		else:
			print('Respuesta del servidor:')
			print('HTTP status_code:', response.status_code)
			re_html = re.sub(r'testImage_.*\.jpeg', 'testImage.jpeg', response.content.decode())
			print('HTML:', re_html)
			ret_val = True
			html_hash = hashlib.md5(str.encode(re_html)).hexdigest()
			if html_hash != '3b31c0ae732ef2e717115754694bd1e9':
				print('El hash MD5 del archivo HTML no es el esperado. Recibido:', html_hash)
				ret_val = False
			print('===FIN PRUEBA DE ELIMINACIÓN DE RECETAS===\n')
			return True

	def test_all(self):
		ret_val = True
		create_status = "[SUCCESS]"
		edit_status = "[SUCCESS]"
		index_status = "[SUCCESS]"
		delete_status = "[SUCCESS]"
		if not self.Test_create():
			ret_val = False
			create_status = "[FAILED]"
			print("FAILED CREATION TEST")
		if not self.Test_edit():
			edit_status = "[FAILED]"
			ret_val = False
			print("FAILED EDIT TEST")
		if not self.Test_index():
			index_status = "[FAILED]"
			ret_val = False
			print("FAILED READ TEST")
		if not self.Test_delete():
			delete_status = "[FAILED]"
			ret_val = False
			print("FAILED DELETE TEST")
		if ret_val:
			print("CREATION TEST\t\t\t " + create_status)
			print("EDIT TEST\t\t\t " + edit_status)
			print("READ TEST\t\t\t " + index_status)
			print("DELETE TEST\t\t\t " + delete_status)

		return ret_val
