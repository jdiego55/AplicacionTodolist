import boto3
import random
import json
from tarea import Tarea

dynamo = boto3.client('dynamodb')

class GestorTareas:
    def __init__(self):
        self.tareas = []
    

    def agregar_tarea(self, nombre):
        completado='Pendiente'
        nombre_tabla='tareas'
        numero=random.randint(1,500)
        datos={'id':{'S':str(numero)},
              'nombre':{'S':str(nombre)},
              'completado':{'S':str(completado)}
              
        }
        response = dynamo.put_item(TableName=nombre_tabla,Item=datos)

    def eliminar_tarea(self, nombre):
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre]

    def completar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.completada = True

    def ver_tareas_pendientes(self):
        nombre_tabla='tareas'
        response = dynamo.scan(
            TableName=nombre_tabla)
        tareas = response.get('Items', [])
        tareas_json = [json.dumps(tarea) for tarea in tareas]
        return tareas_json
