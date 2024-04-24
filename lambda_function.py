import json
import boto3
from gestor_tareas import GestorTareas


def lambda_handler(event, context):
    gestor = GestorTareas()
    # Verificar si la solicitud es GET y la ruta es /consultarTarea
    if event['requestContext']['http']['method'] == 'GET' and event['requestContext']['http']['path'] == '/verTareas':
        tareas_pendientes = gestor.ver_tareas_pendientes()
        tareas_respuesta=''
        if tareas_pendientes:
                for tarea in tareas_pendientes:
                    tareas_respuesta=tareas_respuesta+' - '+tarea
                return {
                    'statusCode': 200,
                    'body': json.dumps('Tareas Pendientes: '+str(tareas_respuesta))
                }
        else:
            return {
                    'statusCode': 404,
                    'body': json.dumps('No hay tareas pendientes')
            }
       
    elif event['requestContext']['http']['method'] == 'POST' and event['requestContext']['http']['path'] == '/agregarTarea':
        # Obtener los datos del cuerpo de la solicitud
        body= event['body']
        body_json = json.loads(body)
        nombre_tarea = body_json.get('nombre')
        gestor.agregar_tarea(nombre_tarea)
        return {
            'statusCode': 200,
            'body': json.dumps('Tarea agregada con nombre '+ str(nombre_tarea))
        }
    elif event['requestContext']['http']['method'] == 'POST' and event['requestContext']['http']['path'] == '/completarTarea':
        # Obtener los datos del cuerpo de la solicitud
        body= event['body']
        body_json = json.loads(body)
        id_tarea = body_json.get('id')
        gestor.completar_tarea(id_tarea)
        return {
            'statusCode': 200,
            'body': json.dumps('Tarea completada con id '+ str(id_tarea))
        }
    elif event['requestContext']['http']['method'] == 'POST' and event['requestContext']['http']['path'] == '/eliminarTarea':
        # Obtener los datos del cuerpo de la solicitud
        body= event['body']
        body_json = json.loads(body)
        id_tarea = body_json.get('id')
        gestor.eliminar_tarea(id_tarea)
        return {
            'statusCode': 200,
            'body': json.dumps('Tarea eliminada con id '+ str(id_tarea))
    }

