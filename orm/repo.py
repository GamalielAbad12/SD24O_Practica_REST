import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

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
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id).all()

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def obtener_fotos_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.fotos WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id).all()

#SELECT * FROM app.calificaciones
def obtener_calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

#SELECT * FROM app.calificaciones WHERE id=alumno
def obtener_calificaciones_alumno_id(id:int, sesion:Session):
    print("SELECT * FROM app.calificaciones WHERE id={id_al}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id).all()

#SELECT * FROM app.calificaciones WHERE id=id-cal
def obtener_calificaciones_id(id:int, sesion:Session):
    print("SELECT * FROM app.calificaciones WHERE id={id_cal}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id).all()

#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def eliminar_alumnos_id(id:int, sesion:Session):
    print("DELETE FROM app.alumnos WHERE id_alumnos={id_al}")
    alumno_id = obtener_alumnos_id(id, sesion)
    if alumno_id is not None:
        sesion.delete(alumno_id)
        sesion.commit() 
    
    return {"mensaje": "Usuario eliminado"}

#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def eliminar_calificaciones_alumnos_id(id:int, sesion:Session):
    print("DELETE FROM app.calificaciones WHERE id_alumnos={id_al}")
    calificaciones_alumno_id = obtener_calificaciones_alumno_id(id, sesion)

    if calificaciones_alumno_id is not None: 
        for calificaciones_alumno in calificaciones_alumno_id:
            sesion.delete(calificaciones_alumno)
        sesion.commit()
    
    respuesta = {"mensaje" : "Calificciones del alumno eliminadas"}
    return respuesta

#DELETE FROM app.fotos WHERE id_alumnos={id_al}
def eliminar_fotos_alumnos_id(id:int, sesion:Session):
    print("DELETE FROM app.fotos WHERE id_alumnos={id_al}")
    fotos_alumno_id = obtener_fotos_alumnos_id(id, sesion)

    if fotos_alumno_id is not None: 
        for fotos_alumno in fotos_alumno_id: 
            sesion.delete(fotos_alumno)
        sesion.commit()
   
    respuesta = {"mensaje" : "Fotos del alumno eliminadas"}
    return respuesta

