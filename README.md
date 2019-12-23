1 ENTORNO VIRTUAL WINDOWS 

para las configuraciones de la carpeta donde se va a trabajar habilitar el entorno
python -m venv .env
call .env\Scripts\activate.bat
deactivate

2 crear un directorio platzigram 
mkdir platzigram
cd platzigram
para activar nuestro ambiente virtual creado 

call ..\.env\Scripts\activate.bat

3. instalar django y verificar librerias en nuestro entorno

pip install Django==2.2.7
pip freeze # para mirar la version de django instalada
django-admin => muestra los comandos de administrador

4. configurar una url con http response para imprimir "Hola Mundo" en urls.py crear la funcion hello_world 
aca no se configura vista adicional. 

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse 

#funcion para la vista Hola Mundo
def hello_word(request):
    return HttpResponse('Hello_world')


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-word/', hello_word)
]

5. crear un nuevo archivo views.py dentro del proyecto platzygram para personalizar nuestra vista de saludo
"""Platzygram views"""

from django.http import HttpResponse 

#funcion para la vista Hola Mundo
def hello_word(request):
    """Return a greeting"""
    return HttpResponse('Hello_world')

6. configurar la vista para traer la hora del servidor

from datetime import datetime

def hello_word(request):
    """Return a greeting"""
    #=> para traer la hora del servidor
    now = datetime.now()
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now= str(now)))

6. como realizar una peticion GET desde la url y obtener numeros ingresados por medio de esa url 
#pasar argumentos desde una url

def hi(request):
    """ Hi."""
    numbers = request.GET['numbers']
    #import pdb; pdb.set_trace()#coloca un debuger en la consola 
    return HttpResponse(str(numbers))

http://localhost:8000/hi/?numbers=10,4,50,32

7. para ordenar la peticion de numeros en url y retornar un .json
def hi(request):
    """ Hi."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb; pdb.set_trace()#coloca un debuger en la consola 
    data={
        'status':'ok',
        'numbers': sorted_ints,
        'message':'Integers sorted successfully.'
    }
    #return HttpResponse(str(numbers), content_type='aplication/json')
    #===============================
    #=>traducir un diccionaro a json
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

8. crear una funcion en views que recibe prametros de una url, se hace una verificaion 

def say_hi(request, name, age):
    '''Return a greeting'''
    if age < 12:
        message='Sorry {}, you are not allowed here'.format(name)
    else:
        message='Hi {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-word/', views.hello_word),
    path ('sorted/',views.sort_integers),
    path('hi/<str:name>/<int:age>', views.say_hi), 
]

http://localhost:8000/hi/Deisy/11

9. creacion de aplicativo posts y configuracion de apps.py
python manage.py startapp posts


from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''Posts aplication settings '''
    name = 'posts'
    varbose_name = 'Posts'


INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'posts', 
]

###################################################################
configuracion de vistas locales en urls.py de nuestro modulo local

from platzigram import views as local_views

path('hello-word/', local_views.hello_word),
path ('sorted/',local_views.sort_integers),
path('hi/<str:name>/<int:age>', local_views.say_hi), 

10. ORM Django
python manage.py shell

>>> from posts.models import User
>>> platzi_users = User.objects.filter(email__endswith='@gmail.com')
>>> platzi_users
<QuerySet [<User: deisy@gmail.com>]>
>>> users = User.objects.all()
>>> users
<QuerySet [<User: >, <User: jjmuesesq@unal.edu.co>, <User: deisy@gmail.com>, <User: milena@unal.edu.co>]>	

>>> for u in users:
...     print(u.email, ':', u.is_admin) 
... 
 : False
jjmuesesq@unal.edu.co : False
deisy@gmail.com : False
milena@unal.edu.co : False

>>> users = User.objects.all()
>>> users
<QuerySet [<User: >, <User: jjmuesesq@unal.edu.co>, <User: deisy@gmail.com>, <User: milena@unal.edu.co>]>
>>> for u in users:
...     print(u.email, ':', u.is_admin)
...
 : False
jjmuesesq@unal.edu.co : False
deisy@gmail.com : True
milena@unal.edu.co : False

Glosario
ORM: Object-relational mapping. Es el encargado de permitir
el acceso y control de una base de datos relacional a través de
una abstracción a clases y objetos.

Templates: Archivos HTML que permiten la inclusión y ejecución
de lógica especial para la presentación de datos.

Modelo: Parte de un proyecto de Django que se encarga de estructurar
las tablas y propiedades de la base de datos a través de clases de Python.

Vista: Parte de un proyecto de Django que se encarga de la
lógica de negocio y es la conexión entre el template y el modelo.

App: Conjunto de código que se encarga de resolver una parte
muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

Patrón de diseño: Solución común a un problema particular.

11. ORM EXPLORANDO MODELO AUTH_USER

Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from django.contrib.auth.models import User
>>> u = User.objects.create_user(username='Sara', password='admin123')
>>> u
<User: Sara>
>>> u.pk
1
>>> u.username
'Sara'
>>> u.password
'pbkdf2_sha256$150000$r6hzTkGSu0Hu$2JYfyjlLr9oJU9KIrF1Vqmp4ahFtXwYNF5ikA7T6uzc='

#CREAR SUPERUSER