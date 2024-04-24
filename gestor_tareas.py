import boto3
import random
import json

dynamo = boto3.client('dynamodb')

class GestorTareas:

    def agregar_tarea(self, nombre):
        completado='Pendiente'
        nombre_tabla='tareas'
        numero=random.randint(1,500)
        datos={'id':{'S':str(numero)},
              'nombre':{'S':str(nombre)},
              'completado':{'S':str(completado)}
              
        }
        response = dynamo.put_item(TableName=nombre_tabla,Item=datos)

    def eliminar_tarea(self, id):
        nombre_tabla='tareas'
        clave_primaria = {'id': {'S': id}}
        response =dynamo.delete_item(
            TableName=nombre_tabla,
            Key=clave_primaria
        )

    def completar_tarea(self, id):
        nombre_tabla='tareas'
        completado='Completado'
        clave_primaria = {'id': {'S': id}}  
        expresion_actualizacion = "SET completado = :val" 
        valores_actualizacion = {":val": {"S": completado}}  

        response = dynamo.update_item(
            TableName=nombre_tabla,
            Key=clave_primaria,
            UpdateExpression=expresion_actualizacion,
            ExpressionAttributeValues=valores_actualizacion
        )       

    def ver_tareas_pendientes(self):
        nombre_tabla='tareas'
        valor_filtrado = 'Pendiente'
        expresion_filtro = "completado = :val"
        expresion_valores = {":val": {"S": valor_filtrado}}
        response = dynamo.scan(
            TableName=nombre_tabla,
            FilterExpression=expresion_filtro,
            ExpressionAttributeValues=expresion_valores
        )
        tareas = response.get('Items', [])
        tareas_json = [json.dumps(tarea) for tarea in tareas]
        return tareas_json
