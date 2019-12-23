"""Platzygram views"""
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

#json
import json

#==================================================
#funcion para la vista Hola Mundo

def hello_word(request):
    """Return a greeting"""
    #=> para traer la hora del servidor
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now= now))

def sort_integers(request):
    """ Return a JSON response with sorted integers."""
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
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    '''Return a greeting'''
    if age < 12:
        message='Sorry {}, you are not allowed here'.format(name)
    else:
        message='Hi {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)

#===================
#TAREA
#regresar la lista de numeros ordenada