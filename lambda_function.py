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

def main():
    #gestor = GestorTareas()
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            nombre_tarea = input("Ingrese el nombre de la tarea que desea agregar: ")
            gestor.agregar_tarea(nombre_tarea)
            print("Tarea agregada correctamente.")
        elif opcion == "2":
            nombre_tarea = input("Ingrese el nombre de la tarea que desea eliminar: ")
            gestor.eliminar_tarea(nombre_tarea)
            print("Tarea eliminada correctamente.")
        elif opcion == "3":
            nombre_tarea = input("Ingrese el nombre de la tarea que desea completar: ")
            gestor.completar_tarea(nombre_tarea)
            print("Tarea completada correctamente.")
        elif opcion == "4":
            tareas_pendientes = gestor.ver_tareas_pendientes()
            if tareas_pendientes:
                print("Tareas pendientes:")
                for tarea in tareas_pendientes:
                    print("-", tarea)
            else:
                print("No hay tareas pendientes.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
