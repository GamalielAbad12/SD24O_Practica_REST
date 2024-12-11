import orm.modelos as modelos
import orm.esquemas as esquemas
from sqlalchemy.orm import Session

#SELECT * FROM app.alumnos
def obtener_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

#SELECT * FROM app.alumnos WHERE id={id_al}
def obtener_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.alumnos WHERE id={id_al}")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id).first()

#SELECT * FROM app.fotos
def obtener_fotos(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()

#SELECT * FROM app.fotos WHERE id={id_fo}
def obtener_fotos_id(id:int, sesion:Session):
    print("SELECT * FROM app.fotos WHERE id={id_fo}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id).first()

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def obtener_fotos_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.fotos WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id).all()

#SELECT * FROM app.calificaciones
def obtener_calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

#SELECT * FROM app.calificaciones WHERE id=alumno
def obtener_calificaciones_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.calificaciones WHERE id={id_al}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id).all()

#SELECT * FROM app.calificaciones WHERE id=id-cal
def obtener_calificaciones_id(id:int, sesion:Session):
    print("SELECT * FROM app.calificaciones WHERE id={id_cal}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id).first()

#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def eliminar_alumnos_id(id:int, sesion:Session):
    print("DELETE FROM app.alumnos WHERE id_alumnos={id_al}")
    alumno_id = obtener_alumnos_id(id, sesion)
    if alumno_id is not None:
        eliminar_calificaciones_alumnos_id(id, sesion)
        eliminar_fotos_alumnos_id(id, sesion)
        sesion.delete(alumno_id)
        sesion.commit() 
    
    respuesta = {"Mensaje": "Usuario eliminado"}
    return respuesta

#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def eliminar_calificaciones_alumnos_id(id:int, sesion:Session):
    print("DELETE FROM app.calificaciones WHERE id_alumnos={id_al}")
    calificaciones_alumno_id = obtener_calificaciones_alumnos_id(id, sesion)

    if calificaciones_alumno_id is not None: 
        for calificaciones_alumno in calificaciones_alumno_id:
            sesion.delete(calificaciones_alumno)
        sesion.commit()
    
    respuesta = {"mensaje" : "Calificaciones del alumno eliminadas"}
    return respuesta

#DELETE FROM app.fotos WHERE id_alumnos={id_al}
def eliminar_fotos_alumnos_id(id:int, sesion:Session):
    print("DELETE FROM app.fotos WHERE id_alumnos={id_al}")
    fotos_alumno_id = obtener_fotos_alumnos_id(id, sesion)

    if fotos_alumno_id is not None: 
        for fotos_alumno in fotos_alumno_id: 
            sesion.delete(fotos_alumno)
        sesion.commit()
   
    respuesta = {"Mensaje" : "Fotos del alumno eliminadas"}
    return respuesta

# DELETE FROM app.fotos WHERE id={id}
def eliminar_fotos_id(id:int, sesion:Session):
    foto_eliminar = obtener_fotos_id(id, sesion)
    print("DELETE FROM app.fotos WHERE id={id}")
    
    if foto_eliminar is not None: 
        sesion.delete(foto_eliminar)
        sesion.commit()
    
    respuesta = {"Menesaje": "Foto eliminada por id"}
    return respuesta    

# DELETE FROM app.calificaciones WHERE id={id}
def eliminar_calificaciones_id(id:int, sesion:Session):
    calificacion_eliminar = obtener_calificaciones_id(id, sesion)
    print("DELETE FROM app.calificaciones WHERE id={id}")

    if calificacion_eliminar is not None:
        sesion.delete(calificacion_eliminar)
        sesion.commit()

    respuesta = {"Mensaje":"Calificación eliminada por id"}
    return respuesta

def agregar_alumnos(alumno_info: esquemas.alumnoBase, sesion:Session):
    alumno_bd = modelos.Alumno()

    alumno_bd.nombre = alumno_info.nombre
    alumno_bd.edad = alumno_info.edad
    alumno_bd.domicilio = alumno_info.domicilio
    alumno_bd.carrera = alumno_info.carrera
    alumno_bd.trimestre = alumno_info.trimestre
    alumno_bd.email = alumno_info.email
    alumno_bd.password = alumno_info.password

    sesion.add(alumno_bd)
    sesion.commit()

    sesion.refresh(alumno_bd)
    return alumno_info