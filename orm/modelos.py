from orm.config import BaseClase
from sqlalchemy import Integer, String, DateTime, Column, ForeignKey
import datetime

class Alumno(BaseClase):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    domicilio = Column(String(100))
    carrera = Column(String(100))
    trimestre = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    fecha_registro = Column(DateTime(timezone=True),default=datetime.datetime.now)

class Calificacion(BaseClase):
    __tablename__ = "calificaciones"
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey(Alumno.id))
    uea = Column(String(100))
    calificacion = Column(String(100))

class Foto(BaseClase):
    __tablename__ = "fotos"
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey(Alumno.id))
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(400))
