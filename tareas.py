def agregar_tarea(id_tarea,descripcion,prioridad):
    for x in tareas:
        if id_tarea == x["id_tarea"]:
            raise ValueError ("la tarea ya existe")
    tarea={
                "id_tarea":id_tarea,
                "descripcion":descripcion,
                "prioridad":prioridad
                }
    tareas.append(tarea)


def actualizar_tarea(id_tarea,nueva_descripcion,nueva_tarea):
    is_exit=""
    for x in tareas:
        if id_tarea == x["id_tarea"]:
            is_exit== id_tarea
            tareas.remove(x)
            tarea={
                
                "id_tarea":id_tarea,
                "descripcion":nueva_descripcion, 
                "prioridad":nueva_tarea
                }
            tareas.append(tarea)
           
            print("la nueva tarea es ", nueva_descripcion," ", "con prioridad ",nueva_tarea  )
    if is_exit == '':
        raise KeyError('la tarea no existe')



def marcar_completada():
    for x in tareas:
            x["completada"]=input(x["descripcion"] +", si esta completada escribir si: ")

def eliminar_tarea(id_tarea):
    is_exit=""
    for x in tareas:
        if id_tarea == x["id_tarea"]:
            is_exit== id_tarea
            print("se elimina ", x["descripcion"])
            tareas.remove(x)
            break
    if is_exit == '':
        raise KeyError('la tarea no existe')


def tareas_pendientes():
    print("lista de tareas pendientes:")
    for x in tareas:
        if x["completada"]!="si":
            print("   " ,x["descripcion"])
            
    print("lista de tareas completadas:")
    for x in tareas:
         if x["completada"]=="si":
            print("   " ,x["descripcion"])


#def listar_tarea(completadas=False):

tareas=[]

agregar_tarea(1,"limpiar",2)
agregar_tarea(2,"cocinar",1)
agregar_tarea(3,"secar",3)
agregar_tarea(4,"tender",4)
print(tareas)
actualizar_tarea(2,"lavar",1)
print(tareas)
eliminar_tarea(1)
print(tareas)
marcar_completada()

print(tareas)

tareas_pendientes()


print(tareas)