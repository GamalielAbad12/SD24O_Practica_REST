import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

#SELECT * FROM app.alumnos
def obtener_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

#SELECT * FROM app.alumnos WHERE id={id_al}
def obtener_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.alumnos WHERE id=id_al")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id).first()

#SELECT * FROM app.fotos
def obtener_fotos(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()

#SELECT * FROM app.fotos WHERE id={id_fo}
def obtener_fotos_id(id:int, sesion:Session):
    print("SELECT * FROM app.fotos WHERE id=id_fo")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id).first()

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def obtener_calificaciones_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos=id_al")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id).all()

#SELECT * FROM app.calificaciones
def obtener_calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

#
def obtener_fotos_alumnos_id(id:int, sesion:Session):
    print("SELECT * FROM app.fotos WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id).all()

#SELECT * FROM app.calificaciones WHERE id=alumno}
def obtener_calificaciones_id(id:int, sesion:Session):
    print("SELECT * FROM app.calificaciones WHERE id=id_alumno")
    return sesion.query(modelos.Calificacion.id)
