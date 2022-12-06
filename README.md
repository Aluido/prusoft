# Pruebas de Software Presentación 1: Testing en Django

## Ejecución
Para poder ejecutar el servidor ocupe los siguientes comandos:
```bash
$ cd presentacion1/
$ python ./manage.py runserver
```

Una vez abierto puede acceder al servidor en la dirección: `localhost:8000/recetas`.
Permitiéndole acceder a las diferentes funcionalidades del programa descritas dentro de `presentacion1/recetas/views.py`.


## Pruebas
Para poder ejecutar el test suite creado ocupe los siguientes comandos:
```bash
$ cd presentacion1/
$ python ./manage.py test
```
Esto mostrará los resultados de las pruebas en su terminal.
La descripción de las pruebas creadas puede ser revisadas en `presentacion1/recetas/tests.py`.

## Observaciones
- El modelo `django.tests.TestCase` corresponde a una subclase de `unittest.TestCase`, demostrando su uso en este framework. (Ref: https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
