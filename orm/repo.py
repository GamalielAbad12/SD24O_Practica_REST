import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

def obtener_alumnos(sesion:Session):
    print("select * from app.usuarios")
    return sesion.query(modelos.Alumno).all()
    
"""
def obtener_alumnos_id():

def obtener_calificaciones_alumnos_id():
"""